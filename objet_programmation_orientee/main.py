# Personne
#   Données : nom, age
#   Actions :
#       Se présenter
#       Demander nom

class Personne:
    type = "Gay"

    def __init__(self, nom : str = "", age : int = 0):
        self.nom = nom
        if self.nom == "":
            self.DemanderNom()
        self.age = age
        if self.age == 0:
            self.DemanderAge()

    def DemanderNom(self) -> None:
        if self.nom == "":
            self.nom = input("Quel est votre nom ? ")
            print(f"Votre nom est {self.nom}.")

    def DemanderAge(self) -> None:
        while self.age == 0:
            try:
                self.age = int(input("Quel est votre age ? "))
            except:
                print("ERREUR : Votre âge doit être un nombre.")
                self.age = 0

    def EstMajeur(self) -> bool:
        return self.age >= 18

    def afficher_informations_personne(self):
        statut = "mineure"
        if self.EstMajeur():
            statut = "majeure"
        info_personne = f"La personne s'appelle {self.nom}"
        if self.age != 0:
            info_personne += f", son age est {self.age} ans et elle est {statut}"
        print(info_personne+".")

    def autre_fonction_niveau_class():
        print("Ceci est une fonction class et pas une fonction instance.")

#Personne.autre_fonction_niveau_class()

personne1 = Personne("Jean", 30)
print(personne1.type)
personne1.type = "Hétéro"
print(personne1.type)
Personne.type = "Re-gay"
print(Personne.type)
print(personne1.type)
personne2 = Personne("Paul", 15)
#personne3.DemanderAge()

liste_personne = []
for i in range(2):
    liste_personne.append(Personne())
for i in range (len(liste_personne)):
    liste_personne[i].afficher_informations_personne()

"""
nom1 = "Jean"
age1 = 30

nom2 = "Paul"
age2 = 25

afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)

nom3 = demander_nom_personne()
age3 = 18

afficher_informations_personne(nom3, age3)
"""


