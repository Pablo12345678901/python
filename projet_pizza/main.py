import random
# pizza ont :
# pizza personalisée
# saisie des ingrédients au fur et à mesure
# enter pour terminer
# cela passe à la pizza suivante
# ensuite pizza s'affiche avec nom : prix
# et ligne d'après liste d'ingrédients
# précision si végétarienne = affiché
# à la fin de la liste, les pizzas personnalisée s'affiche
# leur prix dépend du nombre d'ingrédient

# fonction mélanger :
def melanger(list, nombre=-1) -> list:
    list = list
    if nombre == -1:
        nombre = len(list)
    nombre = test_nombre(nombre, list)
    #print(nombre)
    list_melangee = ["" for each in range(nombre)]
    for i in range(nombre):
        while True:
            index = random.randint(0,len(list)-1)
            if list_melangee[i] == "":
                ###
                if not(list_melangee.count(list[index]) == 1):
                    list_melangee[i] = list[index]
                    break
            #print(list_melangee)
    #print(list_melangee)
    return list_melangee

# test si nombre est inclus entre le min et max de l'intervalle
def test_nombre(nombre_teste, list):
    while True:
        try:
            nombre = int(nombre_teste)
        except:
            print(f"Erreur, ceci n'est pas un nombre. Veuillez saisir un nombre entre 1 et {len(list)}.")
        else:
            if not (1 <= nombre <= len(list)):
                print(f"Erreur : le nombre n'est pas inclus entre 1 et {len(list)}.")
            else:
                return nombre
        nombre_teste = input("Quel nombre choisissez-vous ? ")

"""

class Pizza():
    compteur = 0
    def __init__(self, nom = "Personalisée ", ingredients = [], prix = 9, vegetarienne = False):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix
        self.vegetarienne = vegetarienne
        if self.nom == "Personalisée ":
            Pizza.compteur += 1
            self.nom += str(Pizza.compteur)
            self.ingredients = []
            self.ingredients = self.ajout_ingredients()
        else:
            self.compteur = ""
        if self.prix == 9:
            self.prix = self.modification_prix()

    def afficher_pizza(self):
        check_vegan = ""
        if self.vegetarienne:
            check_vegan = "- VÉGÉTARIENNE"
        print("PIZZA", self.nom, ":", self.prix, "CHF", check_vegan)
        ingredient = ", ".join(self.ingredients)
        print(ingredient)
        print()

    def modification_prix(self):
        self.prix += round(len(self.ingredients)*0.6, 2)
        return self.prix

    def ajout_ingredients(self):
        print(f"Ingrédients pour la pizza {self.nom}")
        while True:
            self.ingredients.append(input("Quel ingrédient souhaitez-vous ajouter ? Taper entrée pour stopper. "))
            print()
            #print(list(self.ingredients))
            if self.ingredients[-1] == "":
                del self.ingredients[-1]
                #print(list(self.ingredients))
                return self.ingredients

liste_pizza = []
liste_pizza.append(Pizza(nom = "4 fromages", ingredients = ["brie", "emmental", "compté", "parmesan"], prix = 8.5, vegetarienne = True))
liste_pizza.append(Pizza(nom = "Hawai", ingredients = ["tomate", "ananas", "oignons"], prix = 9.5))
liste_pizza.append(Pizza(nom = "4 saisons", ingredients = ["oeuf", "emmental", "tomate", "jambon", "olives"], prix = 11))
liste_pizza.append(Pizza(nom = "Végétarienne", ingredients = ["champignons", "tomate", "oignons", "poivrons"], prix = 7.8, vegetarienne = True))

while True:
    liste_pizza.append(Pizza())
    test = input("Voulez-vous créer une autre pizza personnalisée ? Taper entrée pour stopper. ")
    print()
    if test == "":
        break

for pizza in liste_pizza:
    pizza.afficher_pizza()
"""




#"""
class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Afficher(self):
        affichage = f"PIZZA {self.nom} - {self.prix} CHF"
        if self.vegetarienne:
            affichage += " - VÉGÉTARIENNE"
        print(affichage)
        print(", ".join(self.ingredients))
        print()

class PizzaPersonnalisee(Pizza):
    Compteur = 0
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    def __init__(self):
        super().__init__("Personnalisée n°", 0, [], vegetarienne = False)
        PizzaPersonnalisee.Compteur += 1
        self.nom += str(PizzaPersonnalisee.Compteur)
        print(f"Ingrédient(s) pour la PIZZA {self.nom}")
        self.ingredients = self.demander_ingredients_utilisateur()
        self.prix = self.adaptation_prix()



    def demander_ingredients_utilisateur(self):
        unit = "ingrédient"
        while True:
            ingredient = input("Quel ingrédient souhaitez-vous ajouter ? (ENTER POUR TERMINER) ")
            self.ingredients.append(ingredient)
            if len(self.ingredients) > 1:
                unit = "ingrédients"
            if ingredient == "":
                del self.ingredients[-1]
                print(f"Vous avez {len(self.ingredients)} {unit} : {', '.join(self.ingredients)}.")
                print()
                return self.ingredients
            else:
                print(f"Vous avez {len(self.ingredients)} {unit} : {', '.join(self.ingredients)}.")
                print()

    def adaptation_prix(self):
        #print(f"nombre d'ingrédient(s) : {len(self.ingredients)}")
        return (round(PizzaPersonnalisee.PRIX_DE_BASE + len(self.ingredients)*PizzaPersonnalisee.PRIX_PAR_INGREDIENT,2))

def fonction_tri_personnalise_a_creer(element):
    return len(element.ingredients)


liste_ingredients = ["brie", "emmental", "compté", "parmesan", "focaccia", "oignons", "tomates", "mozzarella"]
liste_pizza = []
liste_pizza.append(Pizza("4 fromages", 8.5, melanger(liste_ingredients, 5), vegetarienne = True))
liste_pizza.append(Pizza("nom2", 2.0, melanger(liste_ingredients, 3)))
liste_pizza.append(Pizza("nom3", 10.0, melanger(liste_ingredients, 4)))
liste_pizza.append(Pizza("nom4", 14.0, melanger(liste_ingredients, 1), vegetarienne = True))
liste_pizza.append(PizzaPersonnalisee())
liste_pizza.append(PizzaPersonnalisee())
# liste_pizza.sort(key=fonction_tri_personnalise_a_creer)



for pizza in liste_pizza:
    pizza.Afficher()

"""
nouvelle_liste = list(reversed(liste_pizza))
for pizza in nouvelle_liste:
    pizza.Afficher()
"""





