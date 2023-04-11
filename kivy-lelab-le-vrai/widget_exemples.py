from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from math import sqrt

Builder.load_file("widget_exemples.kv")

class WidgetsExemple(GridLayout):
    compteur = 1
    mon_texte = StringProperty("Comptez")
    compteur_actif = BooleanProperty(False)
    valeur_initiale_slider = NumericProperty(50)
    #DEBUG print(valeur_initiale_slider.defaultvalue)
    valeur_du_slider = StringProperty(str(valeur_initiale_slider.defaultvalue))

    text_input_str = StringProperty("Toto")

    def on_button_click(self):
        #print("Button click")
        if self.compteur_actif:
            self.mon_texte = str(self.compteur)
            self.compteur += 1

    def on_toggle_button_state(self, widget):
        # ajout d'un argument supplémentaire pour faire référence au widget
        # cf fichier .kv
        print("toggle state " + widget.state)
        if widget.state == "normal":
            self.compteur_actif = False
            print("OFF")
            widget.text = "OFF"
        else:
            self.compteur_actif = True
            print("ON")
            widget.text = "ON"

    def on_switch_active(self, widget):
        # le widget est en paramètre secondaire
        # widget.active est de type boolean - donc besoin de convertir en str
        print("Switch : " + str(widget.active))

    def on_slider_value(self, widget):
        #print("Value : " + str(int(widget.value)))
        self.valeur_du_slider = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text