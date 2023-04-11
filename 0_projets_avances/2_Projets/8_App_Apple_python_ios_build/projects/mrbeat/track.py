from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton


class TrackStepButton(ToggleButton):
    pass

class TrackSoundButton(Button):
    pass

class TrackWidget(BoxLayout):
    def __init__(self, sound, audio_engine, nb_steps, track_source, steps_left_align, max_height_track, **kwargs): # ajout de la variable sound pour gérer le nom des sons à afficher
        # passage de l'audio_engine en paramètres lors de l'initialisation
        super(TrackWidget, self).__init__(**kwargs)

        # INITIALISATION DE L'UI
        self.audio_engine = audio_engine # initialisation du paramètre audioengine
        self.sound = sound # initialisation du paramètre son
        self.track_source = track_source

        # CREATION D'UN BOXLAYOUT QUI CONTIENDRA LE NOM DE PISTE ET LE SEPARATEUR AVANT LES STEPS
        sound_and_separator_layout = BoxLayout()
        sound_and_separator_layout.size_hint_x = None # libération de la largeur du boxlayout
        sound_and_separator_layout.width = steps_left_align # détermination de la taille du boxlayout
        self.add_widget(sound_and_separator_layout) # ajout du boxlayout au Mainwidget

        # CREATION DE BOUTONS POUR LES PISTES (AVEC LE STYLE DES TRACKSTEPBUTTON)
        sound_button = TrackSoundButton()
        sound_button.text = sound.displayname # adaptation du displayname du bouton
        sound_button.on_press = self.on_sound_button_press # gestion du clic sur bouton
        sound_and_separator_layout.add_widget(sound_button) # ajout du bouton avec le nom adapté dans le boxlayout

        # CREATION SEPARATEUR ENTRE LES TITRES DES TRACKS ET LES STEPS
        separator_image = Image(source = "RESOURCES/images/track_separator.png")
        separator_image.size_hint_x = None
        separator_image.width = dp(15)
        sound_and_separator_layout.add_widget(separator_image) # ajout du séparateur dans le boxlayout

        self.step_buttons = [] # création d'une liste qui contiendra les step_button
        self.nb_steps = nb_steps

        for i in range(0, nb_steps):
            step_button = TrackStepButton()
            step_button.bind(state=self.on_step_button_state) # lier le bouton à son état via une fonction

            # Différencier les groupes de 4 (le premier et troisième sont similaire mais ils sont différent du 2ème et 4ème qui eux sont similaire et ainsi de suite
            if int(i/4) % 2 == 0: # si l'index divisé par 4 arrondi à l'int inférieur est pair
                step_button.background_normal="RESOURCES/images/step_normal1.png"
            else: # sinon si impair
                step_button.background_normal = "RESOURCES/images/step_normal2.png"

            self.step_buttons.append(step_button) # ajout du step_button à la liste
            self.add_widget(step_button) # ajout du bouton dans le trackwidget à chaque boucle

        self.size_hint_max_y = max_height_track

    def on_step_button_state(self, widget, value):
        steps = []  # le tableau contenant les 1 et 0 selon que les boutons soient enfoncés
        for i in range(0, self.nb_steps):
            if self.step_buttons[i].state == "down": # down = enfoncé = 1
                steps.append(1) # ajout de la valeur du bouton au tableau
            else: # normal = pas enfoncé = 0
                steps.append(0) # ajout de la valeur du bouton au tableau
        self.track_source.set_steps(steps) # ajout de la liste des états au track

    def on_sound_button_press(self):
        self.audio_engine.play_sound(self.sound.samples) # joue le son lors du clic

