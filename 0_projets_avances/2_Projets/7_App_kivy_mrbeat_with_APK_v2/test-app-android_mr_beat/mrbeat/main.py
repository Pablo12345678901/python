# GESTION TAILLE FENÊTRE DE JEU AU DEMARRAGE
from kivy import Config
from kivy.uix.widget import Widget

Config.set('graphics', 'width', '780')
Config.set('graphics', 'height', '360')
Config.set('graphics', 'minimum_width', '700')
Config.set('graphics', 'minimum_height', '300')



# IMPORT
from kivy.metrics import dp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, BooleanProperty, NumericProperty, Clock

# IMPORT DE FICHIER
Builder.load_file("track.kv")
Builder.load_file("play_indicator.kv")
from track import TrackWidget # import de la class TrackWidget depuis le fichier track.py
from sound_kit_service import SoundKitService
from audio_engine import AudioEngine

TRACK_NB_STEPS = 16
MIN_BPM = 80
MAX_BPM = 160


class VerticalSpacingWidget(Widget):
    pass


# CREATION DU MAIN WIDGET
class MainWidget(RelativeLayout):
    tracks_layout = ObjectProperty() # variable qui correspond au BoxLayout du fichier principal.kv
    play_indicator_widget = ObjectProperty() # variable qui correspond au BoxLayout de l'avancement du curseur sur les steps du fichier principal.kv
    TRACK_STEPS_LEFT_ALIGN = NumericProperty(dp(120)) # largeur de la première colonne
    step_index = 0 # création d'une variable pour mémoriser le step_index = le step où on en est
    bpm = NumericProperty(120) # gestion du bpm dans une variable
    change_value_on_bpm_button_click = NumericProperty(5)
    nb_tracks = NumericProperty(0)
    max_height_track = NumericProperty(dp(90))

    # FONCTION D'INITIALISATION
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.sound_kit_service = SoundKitService() # initialisation du soundkitservice
        self.nb_tracks = self.sound_kit_service.get_nb_tracks()
        self.audio_engine = AudioEngine() # initialisation d'un audio_engine
        self.mixer = self.audio_engine.create_mixer(self.sound_kit_service.soundkit.get_all_samples(), self.bpm, TRACK_NB_STEPS, self.on_mixer_current_step_changed, MIN_BPM)

    def on_play_button_pressed(self): # en cas de clic
        self.mixer.audio_play() # appel de la fonction du audio_source_mixer

    def on_stop_button_pressed(self): # en cas de clic
        self.mixer.audio_stop() # appel de la fonction du audio_source_mixer

    # FONCTION QUI S'EXECTUE AUTOMATIQUEMENT A CHAQUE CHANGEMENT DE LA VALEUR DU BPM
    def on_bpm(self, widget, value):
        if value < MIN_BPM:
            self.bpm = MIN_BPM
            return # sortie de la fonction
        if value > MAX_BPM:
            self.bpm = MAX_BPM
            return # sortie de la fonction
        # si je ne suis pas dans un des 2 cas ci-dessus
        # alors j'adapte le bpm
        self.mixer.set_bpm(self.bpm)
        return

    # FONCTION D'AJOUT DES TRACKWIDGET AU BOXLAYOUT DU MAINWIDGET
    def on_parent(self, widget, parent):
        self.play_indicator_widget.set_nb_steps(TRACK_NB_STEPS)

        for i in range(0, self.sound_kit_service.get_nb_tracks()): # boucle sur le nombre de track
            sound = self.sound_kit_service.get_sound_at(i)
            self.tracks_layout.add_widget(VerticalSpacingWidget()) # ajout d'un widget avant chaque tracks pour créer un espace entre eux
            self.tracks_layout.add_widget(TrackWidget(sound, self.audio_engine, TRACK_NB_STEPS, self.mixer.tracks[i], self.TRACK_STEPS_LEFT_ALIGN, self.max_height_track)) # ajout d'un trackwidget au BoxLayout par boucle
        self.tracks_layout.add_widget(VerticalSpacingWidget())  # ajout d'un widget à la fin des tracks pour créer un espace en bas

    def on_mixer_current_step_changed(self, step_index):
        self.step_index = step_index
        Clock.schedule_once(self.update_play_indicator_cbk, 0) # appel de la fonction immédiatement au temps X seconde(s)

    # FONCTION POUR QUE LE MAIN THREAD FASSE LES APPELS ET PAS QU'ON FASSE APPEL A LUI
    def update_play_indicator_cbk(self, dt):
        if self.play_indicator_widget is not None: # tester car deux processus (UI et audioengine) sont en parallèle et pour éviter le bug on test si le processus de UI est terminé ce qui veut dire que le widget a été initialisé
            self.play_indicator_widget.set_current_step_index(self.step_index)

# CREATION DE L'APP
class MrBeatApp(App):
    print("A")
    pass

# LANCEMENT DE L'APP
MrBeatApp().run()