"""
personne = (
    {"nom" : "Pablo", "taille" : 1.72, "age" : 26},
    {"nom" : "Alejandra", "taille" : 1.65, "age" : 41},
)

for i in range(len(personne)):
    print(personne[i]["nom"])
print()
for i in range(len(personne)):
    print(personne[i]["taille"])
"""
#"""

"""
personne = {"nom" : "Pablo", "taille" : 1.72, "age" : 26}
#print(personne["nom"])
personne["nom"] = "Pute"
#print(personne["nom"])
personne['poste'] = "Développeur"
#print(personne)

for i in personne:
    print(i)
print()
for i in personne:
    print(personne[i])
print()
for i in personne:
        print(f"Clef :", i, "/ Valeur :", personne[i])
"""
#"""

"""
personne = {}
personne['poste'] = "Développeur"
print(personne)
# donnera {'poste' : "Développeur"}
# possible d'ajouter un tuple en l'assignant à la valeur d'une clef. Exemple :
achat = (1, 2, 3)
personne["achat"] = achat
print(personne)
# donnera  {'poste' : "Développeur", "achat" : (1, 2, 3)}
"""

"""
def obtenir_informations(nom : str, liste : list):
    for i in liste:
        if nom == i[0]:
            return i
        return None
    
personnes = [
    ("Pablo", 26, 1.72),
    ("Andres", 24, 1.68),
    ("Darryl", 25, 1.88),
    ("Dimitri", 32, 2.02),
]

print(obtenir_informations("Pablo",personnes))
"""
def obtenir_info_personne(nom, dictionnaire):
    try:
        print(nom, dictionnaire[nom])
    except:
        print("Erreur : cette personne n'est pas dans dictionnaire")

personnes = {
    "Pablo" : (26, 1.72),
    "Andres": (24, 1.68),
    "Darryl" : (25, 1.88),
    "Dimitri" : (32, 2.02),
}

obtenir_info_personne("Pablo", personnes)

