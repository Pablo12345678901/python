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
from math import sqrt, ceil




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


class StackLayoutJeuDeLOie(StackLayout):

    # BUT : Création d'un jeux de l'oie avec des numéros de cases
    # qui s'enchaînent en créant une spirale à volonté


    while True:
        # gestion du nombre de cases = unique variable à adapter - le reste se fait tout seul
        total_nb_cases_str = input("Combien de cases souhaiteriez-vous pour ce jeu de l'oie ?\nSaisissez un nombre entier plus grand que 0. >")
        try:
            # gestion du cas : message vide
            if not total_nb_cases_str:
                print("Erreur : vous n'avez rien saisi. Veuillez ré-essayer.\n")
                continue
            # tentative de conversion
            total_nb_cases_int = int(total_nb_cases_str)
            # gestion du nombre <= 0
            if total_nb_cases_int <= 0:
                print("Erreur : vous avez saisi un nombre égal ou inférieur à 0. Veuillez ré-essayer.\n")
                continue
            break
        except:
            print("Erreur : vous n'avez pas saisi un nombre entier Veuillez ré-essayer.\n")

    # calcul du nombre de côté et du nombre de case
    # arrondis à l'entier supérieur pour s'assurer qu'on obtiennent au moins un nombre minimum de côté et de cases permettant d'atteindre le nombre de cases souhaitées
    nb_sides = int(round(ceil(sqrt(total_nb_cases_int)), 0))
    #DEBUG print("nb_sides "+str(nb_sides))
    nb_side_cases = int(round(ceil(sqrt(total_nb_cases_int)), 0))

    # adaptation selon le nombre de cellule restante après l'avant-dernière ligne
    nb_cell_remaining_between_last_square_root_and_further_square_root_of_cases_number = total_nb_cases_int - (nb_sides - 1) ** 2
    #DEBUG print("check " + str(condition_check_for_knowing_last_loop))
    if nb_cell_remaining_between_last_square_root_and_further_square_root_of_cases_number <= nb_sides:
        final_loop = nb_sides - 1
    else:
        final_loop = nb_sides
    final_line_size = total_nb_cases_int - (nb_sides * (final_loop - 1))
    if final_line_size > nb_sides:
        final_loop += 1
        final_line_size -= nb_sides
    #DEBUG print("final_line_size "+str(final_line_size))

    #données pour gestion selon proportion de l'écran
    list_layout_types_and_sizes = [((1, 1),(1 / nb_side_cases, 1 / nb_side_cases),((1, 1 / final_line_size), (1 / final_line_size, 1)),(None,None))]
    list_layout_types_and_sizes_index = 0

    case_side_size = 1 - (1 / nb_side_cases)
    # liste des orientations
    orientations_list = ["rl-bt", "bt-lr", "lr-tb", "tb-rl"]
    # variable pour gestion d'index future de la valeur prise
    # dans la liste ci-dessus
    orientation_list_index = 0
    # variable pour indiquer la taille du layout
    stacklayout_size = [(1, case_side_size), (case_side_size, 1)]
    # variable pour gestion d'index future de la valeur prise
    # dans la liste ci-dessus
    nb_stacklayout_size_index = 0
    case_ref = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # génération du premier layout qui équivaut à l'écran
        # il contiendra tous les layouts suivants
        first_stacklayout = StackLayout(orientation=StackLayoutJeuDeLOie.orientations_list[StackLayoutJeuDeLOie.orientation_list_index], size_hint=StackLayoutJeuDeLOie.list_layout_types_and_sizes[StackLayoutJeuDeLOie.list_layout_types_and_sizes_index][0])
        self.add_widget(first_stacklayout)

        # création d'une liste faussement remplie
        # pour remplacement ultérieur des valeurs par les stacklayouts
        stacklayout_list = []
        stacklayout_list.append(first_stacklayout)
        for i in range(StackLayoutJeuDeLOie.nb_sides):
            stacklayout_list.append("A"+str(i+1))

        StackLayoutJeuDeLOie.orientation_list_index += 1

        # boucle pour ajout des cote
        for i in range(StackLayoutJeuDeLOie.nb_sides):
            # boucle pour ajout des cases sur chaque cote
            for y in range(StackLayoutJeuDeLOie.nb_side_cases):
                if i == (StackLayoutJeuDeLOie.final_loop-1):
                    if stacklayout_list[i].orientation == "bt-lr" or stacklayout_list[i].orientation == "tb-rl":
                        button = Button(text=str(StackLayoutJeuDeLOie.case_ref + 1), size_hint=StackLayoutJeuDeLOie.list_layout_types_and_sizes[StackLayoutJeuDeLOie.list_layout_types_and_sizes_index][2][0])
                    elif stacklayout_list[i].orientation == "rl-bt" or stacklayout_list[i].orientation == "lr-tb":
                        button = Button(text=str(StackLayoutJeuDeLOie.case_ref + 1), size_hint=StackLayoutJeuDeLOie.list_layout_types_and_sizes[StackLayoutJeuDeLOie.list_layout_types_and_sizes_index][2][1])
                else:
                    button = Button(text=str(StackLayoutJeuDeLOie.case_ref + 1), size_hint=StackLayoutJeuDeLOie.list_layout_types_and_sizes[StackLayoutJeuDeLOie.list_layout_types_and_sizes_index][1])

                stacklayout_list[i].add_widget(button)
                StackLayoutJeuDeLOie.case_ref += 1
                # sortie de la boucle de la création de bouton si on atteint la référence du nombre de cases souhaitées
                if StackLayoutJeuDeLOie.case_ref == StackLayoutJeuDeLOie.total_nb_cases_int:
                    break
            # sortie de la boucle de la création de stacklayout si on atteint la référence du nombre de cases souhaitées
            if StackLayoutJeuDeLOie.case_ref == StackLayoutJeuDeLOie.total_nb_cases_int:
                print(f"Félicitation : voici votre jeu de l'oie contenant {StackLayoutJeuDeLOie.total_nb_cases_int} cases !")
                break

            # ajout d'un stacklayout à chaque boucle, avec une orientation
            # d'un quart de tour supplémentaire (sens des aiguilles d'une montre)
            stacklayout_list[i+1] = StackLayout(orientation=StackLayoutJeuDeLOie.orientations_list[StackLayoutJeuDeLOie.orientation_list_index], size_hint=StackLayoutJeuDeLOie.stacklayout_size[StackLayoutJeuDeLOie.nb_stacklayout_size_index])
            stacklayout_list[i].add_widget(stacklayout_list[i+1])

            # incrémentation de +1 pour les variables équivalente
            # aux index de référence des listes tout en haut
            StackLayoutJeuDeLOie.orientation_list_index += 1
            # remise à 0 de l'index s'il atteint le max + 1
            if StackLayoutJeuDeLOie.orientation_list_index == len(StackLayoutJeuDeLOie.orientations_list):
                StackLayoutJeuDeLOie.orientation_list_index = 0
            StackLayoutJeuDeLOie.nb_stacklayout_size_index += 1
            # remise à 0 de l'index s'il atteint le max + 1
            if StackLayoutJeuDeLOie.nb_stacklayout_size_index == len(StackLayoutJeuDeLOie.stacklayout_size):
                StackLayoutJeuDeLOie.nb_stacklayout_size_index = 0

class LeLabApp(App):
    pass

LeLabApp().run()
