# POO EXERCICE DE MISE EN SITUATION 3

# ---
class Chat:
    def __init__(self,nom_facultatif= "inconnu"):
        self.nom = nom_facultatif
        self.SePresenter()

    def SePresenter(self):
        print(f"Bonjour, je suis un chat et je m'appelle {self.nom}.")

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom
        self.SePresenter()

    def SePresenter(self):
        print(f"Bonjour, je suis une personne et je m'appelle {self.nom}.")

class Fils(Chat):
    def __init__(self, nom: str):
        super().__init__(nom)

# ---
chat1 = Chat()
chat2 = Chat("Garfield")

personne = Personne("Jean")
personne_bis = Fils("Renard")
