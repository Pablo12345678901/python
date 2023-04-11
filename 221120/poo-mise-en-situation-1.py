# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme

# corriger bug
# améliorer le code

class Personne:
    def __init__(self, nom: str, age: int, genre: bool = -1):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans.")
        if self.genre == -1:
            return
        genre = "Masculin" if self.genre else "Feminin"
        statut = "mineur" if self.EstMajeur() else "majeur"
        accord = "e" if not self.genre else ""
        print(f"Genre : {genre}")
        print(f"Je suis {statut}{accord}.")
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()