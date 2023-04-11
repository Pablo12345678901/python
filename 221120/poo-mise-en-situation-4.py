# POO EXERCICE DE MISE EN SITUATION 4

# ---

#corriger le None
# améliorer le code pour X personne

class Personne:

    def __init__(self, nom: str = ""):
        self.nom = nom
        self.SePresenter(a)

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
    
l = []
nombre_de_personne = 3
for i in range(nombre_de_personne):
    l.append(Personne(input(f"nom de la personne {i+1} : ")))
