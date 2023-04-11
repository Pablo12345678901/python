from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from math import sqrt


# import de la class depuis le fichier du même nom pour usage ci-dessous
from navigation_screen_manager import NavigationScreenManager
from canvas_exemples import *

class MyScreenManager(NavigationScreenManager):
    # Création d'une class MyScreenManager qui renvoie vers NavigationScreenManage
    # qui est défini dans le fichier du même nom
    # class qu'il faudra importer ci-dessus
    pass

class LeLabApp(App):
    # initialisation de la variable manager à None
    # ainsi la variable sera disponible depuis partout dans le projet
    manager = ObjectProperty(None)
    # la fonction build renvoie l'interface principale
    def build(self):
        # il renverra "MyScreenManager" mais comme il est défini dans le fichier lelab.kv
        # il faut refaire une class ci-dessus
        self.manager = MyScreenManager()
        # ainsi le manager sera accessible depuis partout via : "app.manager"
        return self.manager
        #return CanvasExemple1()
        #return CanvasExemple2()
        #return CanvasExemple3()
        #return CanvasExemple4()
        #return CanvasExemple5()
        #return CanvasExemple6()
        #return CanvasExemple7()

LeLabApp().run()


