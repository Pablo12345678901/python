from audiostream import get_output

from audio_source_mixer import AudioSourceMixer
from audio_source_one_shot import AudioSourceOneShot
from audio_source_track import AudioSourceTrack


class AudioEngine:
    NB_CHANNELS = 1 # 1 = mono - pas stéréo (2)
    SAMPLE_RATE = 44100 # 44100 c'est une convention du nombre de sample par seconde
    BUFFER_SIZE = 1024

    def __init__(self):
        self.output_stream = get_output(channels=self.NB_CHANNELS, rate=self.SAMPLE_RATE, buffersize=self.BUFFER_SIZE) # connexion à la carte son
        self.audio_source_one_shot = AudioSourceOneShot(self.output_stream) # création de l'audio source
        self.audio_source_one_shot.start() # lancement du son


    # CREATION D'UNE FONCTION POUR JOUER LES SONS WAV
    def play_sound(self, wav_samples):
        self.audio_source_one_shot.set_wav_samples(wav_samples) # initialisation des wav_samples et récupération de leur longueur

    def create_track(self, wav_samples, bpm):
        source_track = AudioSourceTrack(self.output_stream, wav_samples, bpm, self.SAMPLE_RATE)
        #source_track.set_steps((1, 0, 0, 1)) # définition de steps en dur pour tester
        source_track.start() # débuter le track
        return source_track

    # FONCTION DE CREATION DU MIXER
    def create_mixer(self, all_wav_samples, bpm, nb_steps, on_current_step_changed, min_bpm):
        source_mixer = AudioSourceMixer(self.output_stream, all_wav_samples, bpm, self.SAMPLE_RATE, nb_steps, on_current_step_changed, min_bpm)
        source_mixer.start() # débuter le mixer
        return source_mixer