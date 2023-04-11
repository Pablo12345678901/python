#2 IMPORTS REQUIS
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from math import sqrt



class MainWidget(Widget):
    pass

class BoxLayoutExemple(BoxLayout):
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        self.add_widget(b1)
        b2 = Button(text="B")
        self.add_widget(b2)
        b3 = Button(text="C")
        self.add_widget(b3)
    """
    pass

class AnchorLayoutExemple(AnchorLayout):
    pass

class GridLayoutExemple(GridLayout):
    pass


class StackLayoutExemple3(StackLayout):

    # BUT : Création d'un jeux de l'oie avec des numéros de cases
    # qui s'enchaînent en créant une spirale à volonté

    # gestion du nombre de côté
    # en adaptant uniquement la variable "taille"
    nombre_cote = 20
    real_size = nombre_cote - 1  # adaptation pour gestion des index ultérieure
    nombre_de_cases_par_cote = 7

    taille_du_cote_cellule = 1 - (1/nombre_de_cases_par_cote)
    # liste des orientations
    orientation_var = ["rl-bt", "bt-lr", "lr-tb", "tb-rl"]
    # variable pour gestion d'index future de la valeur prise
    # dans la liste ci-dessus
    numero_orientation = 0
    # variable pour indiquer la taille du layout
    print(1- (1/nombre_de_cases_par_cote))
    stacklayout_size = [(1, taille_du_cote_cellule), (taille_du_cote_cellule, 1)]
    # variable pour gestion d'index future de la valeur prise
    # dans la liste ci-dessus
    numero_stacklayout_index_size = 0
    compteur_de_case = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # génération du premier layout qui équivaut à l'écran
        # il contiendra tous les layouts suivants
        stacklayout1 = StackLayout(orientation="rl-bt", size_hint=(1, 1))
        self.add_widget(stacklayout1)

        # génération des 10 premières cases du premier layout
        for i in range(StackLayoutExemple3.nombre_de_cases_par_cote):
            #button = Button(text=str(StackLayoutExemple3.compteur_de_case+1), size_hint=(.1, .1))
            button = Button(text=str(StackLayoutExemple3.compteur_de_case+1), size_hint=(1/StackLayoutExemple3.nombre_de_cases_par_cote, 1/StackLayoutExemple3.nombre_de_cases_par_cote))
            stacklayout1.add_widget(button)
            StackLayoutExemple3.compteur_de_case += 1
        StackLayoutExemple3.numero_orientation += 1

        # création d'une liste faussement remplie
        # pour remplacement ultérieur des valeurs par les stacklayouts
        nom = []
        nom.append(stacklayout1)
        for i in range(StackLayoutExemple3.nombre_cote):
            nom.append("A"+str(i+1))
        #DEBUG print(nom)

        # ajout d'un stacklayout à chaque boulce, avec une orientation
        # d'un quart de tour supplémentaire (sens des aiguilles d'une montre)
        for i in range(StackLayoutExemple3.real_size):
            nom[i+1] = StackLayout(orientation=StackLayoutExemple3.orientation_var[StackLayoutExemple3.numero_orientation], size_hint=StackLayoutExemple3.stacklayout_size[StackLayoutExemple3.numero_stacklayout_index_size])
            nom[i].add_widget(nom[i+1])

            # création des cases pour chaque ligne - toutes incluses dans le stacklayout
            for y in range(StackLayoutExemple3.nombre_de_cases_par_cote):
                button2 = Button(text=str(StackLayoutExemple3.compteur_de_case+1), size_hint=(1/StackLayoutExemple3.nombre_de_cases_par_cote, 1/StackLayoutExemple3.nombre_de_cases_par_cote))
                nom[i+1].add_widget(button2)
                StackLayoutExemple3.compteur_de_case += 1

            # incrémentation de +1 pour les variables équivalente
            # aux index de référence des listes tout en haut
            StackLayoutExemple3.numero_orientation += 1
            if StackLayoutExemple3.numero_orientation == 4:
                StackLayoutExemple3.numero_orientation = 0
            StackLayoutExemple3.numero_stacklayout_index_size += 1
            if StackLayoutExemple3.numero_stacklayout_index_size == 2:
                StackLayoutExemple3.numero_stacklayout_index_size = 0

class LeLabApp(App):
    pass

LeLabApp().run()
