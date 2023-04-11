import wave
from array import array


# CREATION D'UNE CLASS POUR CHAQUE SON
class Sound:
    samples = None
    nb_samples = 0
    def __init__(self, filename, displayname):
        # filename : nom du fichier, displayname : le nom qui sera affiché
        self.filename = filename
        self.displayname = displayname
        self.load_sound() # appel de la fonction sur le son

    # RECUPERATION DES SAMPLES DEPUIS LE FICHIER
    def load_sound(self):
        wav_file = wave.open(self.filename, mode='rb') #création d'un fichier au format binaire pour lecture
        self.nb_samples = wav_file.getnframes() # obtenir le nombre de sample (frame) du fichier
        frames = wav_file.readframes(self.nb_samples) # lit et retourne sous forme de bytes (8 bits) le nombre de frames
        self.samples = array('h', frames) # sauvegarde des samples dans l'objet sound


# CLASS GENERIQUE POUR LES SOUNDSKIT
class SoundKit:
    sounds = ()
    # RECUPERATION DU NOMBRE DE PISTES
    def get_nb_tracks(self):
        return len(self.sounds)

    # FONCTION QUI RETOURNE LES SONS
    def get_all_samples(self):
        sounds_list = []
        for i in range(0, len(self.sounds)):
            sounds_list.append(self.sounds[i].samples)
        return sounds_list

# CREATION D'UNE CLASS PAR TYPE DE SON - CLASS SPECIFIQUE POUR CHAQUE SOUNDKIT
# on anticipe l'évolution du projet qui pourrait avoir plusieurs types (et class) de sons
class SoundKit1(SoundKit): # type de sons1 - cette class hérite de SoundKit
    # SOUNDS = la liste des sons
    sounds = (
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
    )


class SoundKit2(SoundKit): # type de sons1 - cette class hérite de SoundKit
    # SOUNDS = la liste des sons
    sounds = (
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
    )

class SoundKit3(SoundKit): # type de sons1 - cette class hérite de SoundKit
    # SOUNDS = la liste des sons
    sounds = (
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
    )

class SoundKit4(SoundKit): # type de sons1 - cette class hérite de SoundKit
    # SOUNDS = la liste des sons
    sounds = (
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
    )

class SoundKit5(SoundKit): # type de sons1 - cette class hérite de SoundKit
    # SOUNDS = la liste des sons
    sounds = (
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/kick.wav", "KICK"),
    )

class SoundKit6(SoundKit): # type de sons1 - cette class hérite de SoundKit
    # SOUNDS = la liste des sons
    sounds = (
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/pluck.wav", "PLUCK"),
        Sound("sounds/kit1/bass.wav", "BASS"),
    )

class SoundKitAll(SoundKit): # type de sons1 - cette class hérite de SoundKit
    # SOUNDS = la liste des sons
    sounds = (
        Sound("sounds/kit1/kick.wav", "KICK"),
        Sound("sounds/kit1/clap.wav", "CLAP"),
        Sound("sounds/kit1/shaker.wav", "SHAKER"),
        Sound("sounds/kit1/snare.wav", "SNARE"),
        Sound("sounds/kit1/pluck.wav", "PLUCK"),
        Sound("sounds/kit1/bass.wav", "BASS"),
        Sound("sounds/kit1/effects.wav", "EFFECTS"),
        Sound("sounds/kit1/vocal_chop.wav", "VOCAL"),
    )



# CREATION D'UNE CLASS POUR GERER TOUTES LES CLASS DE SONS
class SoundKitService:
    # choix du soundkit appelé - il pourrait en avoir plusieurs selon l'évolution du projet
    #soundkit = SoundKit1()# Pour tester avec 4 tracks
    #soundkit = SoundKit2() # Pour tester avec 16 tracks
    #soundkit = SoundKit3()  # Pour tester avec 8 tracks
    #soundkit = SoundKit4()  # Pour tester avec 32 tracks
    #soundkit = SoundKit5() # Pour tester l'overflow avec 16 tracks de kick
    #soundkit = SoundKit6() # Pour tester que le bpm est correct en utilisant des sons d'une durée de 115 bpm exactement
    soundkit = SoundKitAll()  # Pour tester avec tous les tracks (8 sons)

    # RECUPERATION DU NOMBRE DE PISTES
    def get_nb_tracks(self):
        return self.soundkit.get_nb_tracks() # via la fonction au sein du soundkit choisi

    # RECUPERATION DU SON
    def get_sound_at(self, index): # ajout de l'index en paramètres pour adapter le nom du son en fonction de celui-ci
        if index >= len(self.soundkit.sounds): # on se couvre au cas où la fonction est appelée au-delà de l'index max
            return None
        return self.soundkit.sounds[index]