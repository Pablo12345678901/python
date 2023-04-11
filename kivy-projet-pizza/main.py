from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from models import Pizza
from http_client import HttpClient
from storage_manage import StorageManager


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()

class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty()
    # définition de la fonction d'initialisation
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        HttpClient().get_pizza(self.on_server_data, self.on_server_error)

    def on_parent(self, widget, parent):
        dictionaries_list = StorageManager().load_data("pizzas")
        if dictionaries_list: # uniquement si dictionaries_list n'est pas None
            self.recycleView.data = dictionaries_list

    def on_server_data(self, data):
        self.recycleView.data = data
        StorageManager().save_data("pizzas", data)

    def on_server_error(self, error):
        # affichage du message d'erreur
        self.error_str = "ERREUR : " + error

with open("pizzav1.kv", encoding='utf8') as f:
    Builder.load_string(f.read())

class PizzaApp(App):
    def build(self):
        return MainWidget()

PizzaApp().run()