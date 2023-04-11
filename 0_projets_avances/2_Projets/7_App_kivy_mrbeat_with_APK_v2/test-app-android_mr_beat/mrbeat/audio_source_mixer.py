from array import array

from audiostream.sources.thread import ThreadSource

from audio_source_track import AudioSourceTrack

def sum_16bits(n):
    # n est un tuple correspondant à tous les éléments du i ème index des listes
    nb_bits = 16
    s = sum(n) # ici, on additionne ces éléments
    if s > 2**(nb_bits-1)-1:
        s = 2**(nb_bits-1)-1 # plafonnement à la valeur max d'un int signé de 16bits
    elif s < -(2**(nb_bits-1)):
        s = -(2**(nb_bits-1)) # plafonnement à la valeur min d'un int signé de 16bits
    return s


class AudioSourceMixer(ThreadSource):
    # cette classe hérite de ThreadSource
    buf = None

    # Mixer -> starter
    #   get_bytes (appelé par la carte son)
    #   -> AudioSourceTrack (on les start pas)
    #       get_bytes (appelé à la main)
    #   -> AudioSourceTrack (on les start pas)
    #       get_bytes (appelé à la main)
    #   -> AudioSourceTrack (on les start pas)
    #       get_bytes (appelé à la main)
    #   -> AudioSourceTrack (on les start pas)
    #       get_bytes (appelé à la main)

    def __init__(self, output_stream, all_wav_samples, bpm, sample_rate, nb_steps, on_current_step_changed, min_bpm, *args, **kwargs):
        ThreadSource.__init__(self, output_stream, *args, **kwargs) # idem pour le threadsource
        self.tracks = [] # création d'une liste de tracks
        for i in range(0, len(all_wav_samples)): # pour chaque son de la liste
            track = AudioSourceTrack(output_stream, all_wav_samples[i], bpm, sample_rate, min_bpm) # création d'un track par son
            track.set_steps((0, ) * nb_steps) # création d'un tableau vide pour chaque track
            self.tracks.append(track) # mémorisation de chaque tracks dans la liste

        self.buf = None  # création d'un buffer pour retourner le son mixé des tracks
        self.silence = array('h', b"\x00\x00" * self.tracks[0].buffer_nb_samples) # création d'un buffer rempli de silence
        self.nb_steps = nb_steps # initialisation du nb_steps
        self.current_sample_index = 0 # index du dernier sample envoyé
        self.current_step_index = 0 # index du step joué
        self.bpm = bpm # initialisation des bpm
        self.sample_rate = sample_rate # initialisation du sample_rate - équivalent initialement à 44'100
        self.on_current_step_changed = on_current_step_changed
        self.is_playing = False
        self.min_bpm = min_bpm

    def set_steps(self, index, steps):
        if index >= len(self.tracks): # si index non existant (trop grand)
            return
        if not len(steps) == self.nb_steps: # contrôle que le nombre de steps n'a pas changé
            self.tracks[index].set_steps(steps) # pour chaque tracks, gestion des steps

    def set_bpm(self, bpm):
       if bpm < self.min_bpm: # ne pas changer le bpm s'il est inférieur à sa valeur minimale
           return
       self.bpm = bpm

    # FONCTION DE GESTION DE L'ACTIVATION DU TRACK
    def audio_play(self):
        self.is_playing = True # lorsque l'état est true, get_bytes joue le son

    # FONCTION DE GESTION DU STOP DU TRACK
    def audio_stop(self):
        self.is_playing = False # lorsque l'état est false, get_bytes joue le son vide

    # FONCTION DE CHARGEMENT DES NOUVEAUX SAMPLES MIXER ENTRE TOUS LES TRACKS
    def get_bytes(self, *args, **kwargs):

        for i in range(0, len(self.tracks)):
            self.tracks[i].set_bpm(self.bpm)  # adaptation du bpm pour chaque track

        step_nb_samples = self.tracks[0].step_nb_samples

        if not self.is_playing: # si pas play
            return self.silence[0:step_nb_samples].tobytes() # je retourne le buffer complété de sons vides

        track_buffers = []  # création d'un tableau de buffers

        for i in range(0, len(self.tracks)): # boucler sur le nombre de tracks
            track = self.tracks[i]
            track_buffer = track.get_bytes_array() # récupération d'un buffer pour chaque track
            track_buffers.append(track_buffer) # stockage du buffer dans une liste

        """
        for i in range(0, step_nb_samples): # pour chaque step de tous les tracks
            self.buf[i] = 0  # mis à 0 de la i ème valeur du buf
            for j in range(0, len(track_buffers)): # pour tous les buffer
                self.buf[i] += track_buffers[j][i] # récupération du i ème élément et addition car chaque son est une onde qui s'additionne
        """
        s = map(sum_16bits, zip(*track_buffers)) # combinaison des tracks (combinaison des sommes des samples pour chaque track)

        self.buf = array('h', s) # allocation dans le buffer

        # ici on va envoyer le step actuelle à notre PlayIndicator
        if self.on_current_step_changed is not None:
            # Décallage de 2 steps pour synchroniser l'affichage du step
            # courant et le son entendu (à cause des buffers audio)
            step_index_for_display = self.current_step_index - 2 # ajuster visuellement et artificiellement le step actuel
            if step_index_for_display < 0: # si le step est négatif
                step_index_for_display += self.nb_steps # c'est qu'il est à la fin des steps donc on le décalle
            self.on_current_step_changed(step_index_for_display)

        self.current_step_index += 1 # on passe au step suivant
        if self.current_step_index >= self.nb_steps:
            self.current_step_index = 0 # remise à 0 de l'index du step si on a dépassé le nb de step max
        return self.buf[0:step_nb_samples].tobytes() # je retourne le buffer complété