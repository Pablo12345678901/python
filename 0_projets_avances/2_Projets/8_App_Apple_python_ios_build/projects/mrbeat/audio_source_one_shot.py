from array import array

from audiostream.sources.thread import ThreadSource


class AudioSourceOneShot(ThreadSource):
    # cette classe hérite de ThreadSource
    wav_samples = None
    nb_wav_samples = 0
    def __init__(self, output_stream, *args, **kwargs):
        ThreadSource.__init__(self, output_stream, *args, **kwargs) # idem pour le threadsource
        self.chunck_nb_samples = 32 # le nombre de sample à envoyer par chunck
        self.current_sample_index = 0 # index du dernier sample envoyé
        self.buf = array('h', b"\x00\x00" * self.chunck_nb_samples) # création d'un buffer des 64 bytes = 32 samples avec que des "0"

    # INITIALISER LES WAV_SAMPLES
    def set_wav_samples(self, wav_samples):
        self.wav_samples = wav_samples # sauvegarde des wav samples
        self.current_sample_index = 0 # remise à 0 de l'index à chaque appel de la fonction pour pouvoir rejouer deux fois d'affilée un même son - sinon bug
        self.nb_wav_samples = len(wav_samples)  # stockage du nombre des samples

    # FONCTION DE CHARGEMENT DES NOUVEAUX SAMPLES
    def get_bytes(self, *args, **kwargs):
        if self.nb_wav_samples > 0: # si on a un son et donc que la longueur des samples > 0, on l'utilise, sinon, retourne le buf initial avec des 0
            for i in range(0, self.chunck_nb_samples): # boucler sur le nombre de sample du chunck
                """
                # Pour jouer le son en boucle, ajouter ce bout de code :
                if self.current_sample_index >= self.nb_wav_samples:
                    self.current_sample_index = 0 # remise à 0 de l'index donc on repart du premier sample
                """
                if self.current_sample_index < self.nb_wav_samples: # éviter d'aller au delà du dernier sample du wav
                    self.buf[i] = self.wav_samples[self.current_sample_index] # récupération du sample dans le buf = mini buffer pour le chunck - ce n'est pas le buf de 1024 bytes
                else:
                    self.buf[i] = 0 # jouer le son vide (rempli de zéro)
                self.current_sample_index += 1 # décalage de 1 pour passer au sample suivant à chaque boucle
        return self.buf.tobytes() # je retourne le buffer complété