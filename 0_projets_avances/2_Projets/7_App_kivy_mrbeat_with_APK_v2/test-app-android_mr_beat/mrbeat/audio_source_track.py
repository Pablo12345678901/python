from array import array

from audiostream.sources.thread import ThreadSource


class AudioSourceTrack(ThreadSource):
    # cette classe hérite de ThreadSource
    steps = ()
    step_nb_samples = 0

    # DEBUG pour éviter que tous les sons enclenchés ne soient lancé au premier step
    # mêne si celui-ci n'est pas activé
    first_time_start = True

    def __init__(self, output_stream, wav_samples, bpm, sample_rate, min_bpm, *args, **kwargs):
        # mise en paramètres du wav_samples car le son ne changera pas
        # et du bpm pour le rythme auquel sera joué le son
        ThreadSource.__init__(self, output_stream, *args, **kwargs) # idem pour le threadsource
        self.current_sample_index = 0 # index du dernier sample envoyé
        self.current_step_index = 0 # index du step joué
        self.wav_samples = wav_samples # sauvegarde des wav samples
        self.nb_wav_samples = len(wav_samples)  # stockage du nombre des samples
        self.bpm = bpm # initialisation des bpm
        self.sample_rate = sample_rate # initialisation du sample_rate - équivalent initialement à 44'100
        self.last_sound_sample_start_index = 0 # mémoriser l'index du début du son
        self.min_bpm = min_bpm

        self.step_nb_samples = self.compute_step_nb_samples(bpm) # calcul du nombre de samples actuellement utilisés
        self.buffer_nb_samples = self.compute_step_nb_samples(min_bpm) # allocation d'un gros buffer : le buffer maximal - pour qu'on ne soit jamais hors index dans les autres fonctions
        self.silence = array('h', b"\x00\x00" * self.buffer_nb_samples) # un buffer rempli de silence

        if not self.bpm == 0: # on se protège de l'éventuelle division par 0
            n = int(self.sample_rate * 15 / self.bpm)
            if not n == self.step_nb_samples: # si la valeur à changé
                self.step_nb_samples = n # alors on l'adapte sinon on ne fait rien

    def set_steps(self, steps):
        if not len(steps) == len(self.steps): # s'il y a un changement au niveau du nombre de steps
            self.current_step_index = 0  # remise à 0 de l'index du step en cours
        self.steps = steps


    def set_bpm(self, bpm):
        self.bpm = bpm
        self.step_nb_samples = self.compute_step_nb_samples(bpm)

    # CALCUL DU NOMBRE DE SAMPLES PAR STEP
    def compute_step_nb_samples(self, bpm_value):
        # 1 pas = 44'100 * 15 / BPM
        # step_nb_samples = sample_rate * 15 / bpm
        if not bpm_value == 0:
            n = int(self.sample_rate * 15 / bpm_value)
            return n
        return 0

    # FONCTION QUI CONTRÔLE SI TOUS LES STEPS SONT DESACTIVES
    def no_step_activated(self):
        # si tous les steps désactivés ou aucun step
        if not 1 in self.steps or not self.steps:
            return True
        return False

    # FONCTION DE CHARGEMENT DES NOUVEAUX SAMPLES
    def get_bytes_array(self):

        result_buf = None # le buffer à retourner à la fin de la fonction

        # cas 1- Aucun pas d'activé
        if self.no_step_activated():
            # on retourne le silence
            result_buf = self.silence[0:self.step_nb_samples]

        # cas 2 - Si step activé
        elif self.steps[self.current_step_index] == 1:

            # DEBUG pour éviter que tous les sons enclenchés ne soient lancé au premier step
            # mêne si celui-ci n'est pas activé
            self.first_time_start = False

            self.last_sound_sample_start_index = self.current_sample_index  # mémoriser l'index du début du son
            # cas 2.1 - et le son est plus grand que le nombre de samples dans un step
            if self.nb_wav_samples >= self.step_nb_samples:
                result_buf = self.wav_samples[0:self.step_nb_samples] # on joue le son sur la longueur du step
            # cas 2.2 - ou que le son est plus petit que le nombre de samples dans un step
            else:
                silence_nb_samples = self.step_nb_samples - self.nb_wav_samples
                result_buf = self.wav_samples[0:self.nb_wav_samples] # le son avec ses samples
                result_buf.extend(self.silence[0:silence_nb_samples]) # complété de son vide en quantité suffisante pour compléter le step

        # cas 3 - Si step pas activé
        else:
            # mais on doit jouer la suite du son
            index = self.current_sample_index - self.last_sound_sample_start_index  # index actuel du son du fichier wav

            #DEBUG pour éviter que tous les sons enclenchés ne soient lancé au premier step
            # mêne si celui-ci n'est pas activé
            if self.steps[self.current_step_index] == 0 and self.first_time_start:
                result_buf = self.silence[0:self.step_nb_samples]


            # cas 3.1 test : si on a fini de jouer le son
            # if index > self.nb_wav_samples: # ORIGINAL DU PROF

            # DEBUG pour éviter que tous les sons enclenchés ne soient lancé au premier step
            # mêne si celui-ci n'est pas activé
            elif index > self.nb_wav_samples:

                result_buf = self.silence[0:self.step_nb_samples] # on joue le silence
            #   cas 3.2 : si ce qu'il reste à jouer est plus long qu'un step
            elif (self.nb_wav_samples - index) >= self.step_nb_samples:
                result_buf = self.wav_samples[index:self.step_nb_samples + index] # remplissage du buffer de l'index à la taille du step en partant depuis l'index
            #   cas 3.3 : sinon si ce qu'il reste à jouer est plus court qu'un step
            else:
                silence_nb_samples = self.step_nb_samples - (self.nb_wav_samples - index) # calcul du son restant à jouer
                result_buf = self.wav_samples[index:self.nb_wav_samples]
                result_buf.extend(self.silence[0:silence_nb_samples]) # et complétion avec du son vide
        self.current_sample_index += self.step_nb_samples # décallage du current sample step index du nombre de samples dans un step après l'avoir joué

        self.current_step_index += 1 # on passe au step suivant

        if self.current_step_index >= len(self.steps):
            self.current_step_index = 0 # remise à 0 de l'index du step si on a dépassé le step max

        # COUVERTURE CONTRE LE CAS OÙ LE RESULT BUF EST VIDE
        if result_buf is None:
            print("result buf is None")
            #return self.silence[0:self.step_nb_samples]
        # COUVERTURE CONTRE LE CAS OÙ LE RESULT BUF N'A PAS LA BONNE LONGUEUR
        elif not len(result_buf) == self.step_nb_samples:
            print("result buf len is not step_nb_samples")
            #return self.silence[0:self.step_nb_samples]
        return result_buf # je retourne le buffer complété

    def get_bytes(self, *args, **kwargs):
        return self.get_bytes_array().tobytes()

