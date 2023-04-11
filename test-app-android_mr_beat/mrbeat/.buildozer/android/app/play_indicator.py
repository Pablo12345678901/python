from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget


# plus un toggle button mais une image
# basé sur source selon off ou on
# renommé en PlayIndicatorLight
# changer les buttons en "lights"


# GESTION D'UN INDICATEUR QUI S'ALLUME SI LE STEP EST EN COURS
class PlayIndicatorLight(Image):
    pass


class PlayIndicatorWidget(BoxLayout):
    nb_steps = 0 # variable de class pour mémoriser le nombre de step
    lights = [] # création d'une liste pour stocker les valeurs d'activation du step en cours (on / off)
    left_align = NumericProperty(0) # propriété pour décaller les steps de la largeur du titre des tracks
    # Celle-ci est adaptée dans main.py puis appeler via mrbeat.kv

    # ACTIVATION DE LA COULEUR AU DESSUS DU STEP EN COURS
    def set_current_step_index(self, index):
        if index >= len(self.lights): # on se couvre contre un index trop grand
            return
        for i in range(0, len(self.lights)): # Pour chaque bouton de la liste
            light = self.lights[i] # on récupère la lumière
            if i == index: # si l'index en cours est celui du bouton
                light.source = "RESOURCES/images/indicator_light_on.png" # Image du bouton allumé
            else: # sinon
                light.source = "RESOURCES/images/indicator_light_off.png" # Image du bouton éteint


    # FONCTION POUR ADAPTER LE NOMBRE DE STEP DYNAMIQUEMENT
    def set_nb_steps(self, nb_steps):
        if not nb_steps == self.nb_steps: # Si le nb de steps a changé et n'est plus égal à la valeur de la variable de class
            self.lights = [] # vider la liste de boutons afin de ne pas accumuler les boutons en cas de rappel de la fonction
            self.clear_widgets() # supprimer tous les widgets afin de ne pas accumuler les boutons en cas de rappel de la fonction
            dummy_widget = Widget() # faux widget pour décaller les autres boutons de la largeur du titre des tracks
            dummy_widget.size_hint_x = None # flexibiliser la taille de la larrgeur
            dummy_widget.width = self.left_align # définir la taille de la largeur
            self.add_widget(dummy_widget) # ajout du widget au layout

            for i in range(0, nb_steps):
                light = PlayIndicatorLight() # création d'un objet avec l'image de la lumière (on / off)
                light.source = "RESOURCES/images/indicator_light_off.png" # par défaut, avant le démarrage, toutes les lumières sont éteintes
                self.lights.append(light)  # ajout de la lumière à la liste des lumières
                self.add_widget(light)  # ajout du la lumière (image) dans le layout à chaque boucle
            self.nb_steps = nb_steps # adaptation du nombre de steps
