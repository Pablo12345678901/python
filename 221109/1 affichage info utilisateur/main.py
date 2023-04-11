"""
personne = []

nombre_de_personnes = input("Combien de personnes ? ")
nombre_de_personnes_int = int(nombre_de_personnes)

for i in range(nombre_de_personnes_int):
    print("Personne n°", i+1)
    nom = input("Quel est votre nom ? ")
    age = input("Quel est votre âge ? ")
    profil = [nom, age]
    personne.append(profil)

i = 0
for profil in personne:
    i +=1
    print("Personne n°", i, "Prénom", profil[0], "Âge", profil[1], "ans")
"""





"""
def recuperer_et_afficher_infos_personnes(personne):
    print("Personne n°", personne)
    nom = input("Quel est votre nom ? ")
    age = int(input("Quel est votre âge ? "))
    return nom,age


def afficher_infos_personne(nom="", age=0):
    print("La personne est", nom + ", et son âge est", age, "ans.")
    print(f"Son prénom comporte {len(nom)} caractères.")

def est_majeur(age, age_majorite):
    if age >= 18:
        print("Cette personne a", age, "ans et est majeure.")
    else:   
        print("Cette personne a", age, "ans et est mineure.")


nom = ""
age = 0
age_majorite = 18
nombre_personnes_int = int(input("Combien de personnes ? "))
personne = 0



for i in range(nombre_personnes_int):
    personne +=1
    profil = recuperer_et_afficher_infos_personnes(personne)
    afficher_infos_personne(profil[0], profil[1])
    est_majeur(profil[1],age_majorite)
"""




"""
def recuperer_et_afficher_infos_personnes(personne):
    print("Personne n°", personne)
    nom = input("Quel est votre nom ? ")
    age = int(input("Quel est votre âge ? "))
    return nom,age


def afficher_infos_personne(nom="", age=0):
    print("La personne est", nom + ", et son âge est", age, "ans.")
    print(f"Son prénom comporte {len(nom)} caractères.")

def est_majeur(age, age_majorite):
    if age >= 18:
        print("Cette personne a", age, "ans et est majeure.")
    else:   
        print("Cette personne a", age, "ans et est mineure.")


nom = ""
age = 0
age_majorite = 18
nombre_personnes_int = int(input("Combien de personnes ? "))
personne = 0



for i in range(nombre_personnes_int):
    personne +=1
    profil = recuperer_et_afficher_infos_personnes(personne)
    afficher_infos_personne(profil[0], profil[1])
    est_majeur(profil[1],age_majorite)
"""

"""
recuperer_et_afficher_infos_personnes
    -> recuperer_infos_personnes
    -> afficher_infos_personnes
        -> est_majeur


"""


def recuperer_et_afficher_infos_personnes(personne : int):
    print("Personne n°", personne)
    nom, age = recuperer_infos_personnes(personne)
    afficher_infos_personnes(personne,nom, age)


def recuperer_infos_personnes(personne : int) -> (str, int):
    nom = input("Quel est votre nom ? ")
    age = int(input("Quel est votre âge ? "))
    return nom, age

def afficher_infos_personnes(personne : int, nom : str, age : int) -> None:
    print("La personne", personne, "est", nom + ", et son âge est", age, "ans.")
    print(f"Son prénom comporte {len(nom)} caractères.")
    est_majeur(age)

def est_majeur(age: int) -> None:
    if age >= 18 :
        print("Cette personne a", age, "ans et est majeure.")
        return None
    print("Cette personne a", age, "ans et est mineure.")
    

nombre_personnes = 12

for i in range (nombre_personnes):
    recuperer_et_afficher_infos_personnes(i+1)




"""
nombre_personne = input("Combien de personne ? ")
nombre_personne_int = int(nombre_personne)

for i in range (nombre_personne_int):
    recuperer_et_afficher_infos_personnes(i+1)
"""