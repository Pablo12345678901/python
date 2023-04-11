# POO EXERCICE DE MISE EN SITUATION 2
class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + self.nom)
        self.SePresenter()

    def SePresenter(self, ):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print(f"Bonjour, je m'appelle  {self.nom} j'ai {self.age} ans.")
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25)
personne2 = Personne("Emilie", 17)