
# cette class n'hérite pas des éléments de Kivy
# donc pas besoin de mettre les ** et **kwargs
class Pizza:
    # initialisation des paramètres de la class pizza selon leur type
    nom = ""
    ingredients = ""
    prix = 0.0
    vegetarienne = False

    def __init__(self, nom, ingredients, prix, vegetarienne):
        # pas besoin d'appeler le "super" dans le __init__ car
        # cette class n'hérite de personne
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix
        self.vegetarienne = vegetarienne

    def get_dictionnary(self):
        return {
            "nom" : self.nom,
            "ingredients" : self.ingredients,
            "prix" : self.prix,
            "vegetarienne" : self.vegetarienne
        }