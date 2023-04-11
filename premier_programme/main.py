"""
banzai = 10
variable = banzai<=5
print(variable)
# cela donnera False
"""


"""
def numero_personne() :
    global personne
    personne +=1
    print("Personne n° " + str(personne))
"""


print("""Texte
sur
plusieurs
lignes""")


print("toto", 10, "Jacques", 15.2)





def afficher_information_personne(nom, age, taille=0) :
    print()
    print("Vous vous appelez " + nom + " et avez " + str(age) + " ans.")
    print(f"Vous vous appelez {nom} et avez {age} ans.")
    print(f"Vous vous appelez %s et avez %s ans." % (nom,age) )
    print("L'an prochain, vous aurez " + str(age+1) + " ans.")

    if age == 1 or age == 2 :
        print("Vous êtes bébé.")
    elif age < 10 :
        print("Vous êtes enfant.")
    elif 12 <= age < 17 :
        print("Vous êtes adolescent.")
    #elif age < 17:
    #    print("Vous êtes mineur.")
    elif age == 17 :
        print("Vous êtes presque majeur.")
    elif age == 18:
        print("Tout juste majeur : Félicitation.")
    elif age > 60:
        print("Vous êtes sénior.")
    elif age > 18:
        print("Vous êtes majeur.")

    print()

    #afficher la taille
    if taille != 0 :
        print("Vous mesurez " + str(taille) + " m.")



# demander le nom
def demander_nom():
    reponse_nom = input("Quel est votre nom ? ")
    while reponse_nom == "":
        reponse_nom = input("Veuillez saisir votre nom.")
    return reponse_nom


# demander l'âge
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_int = input("Quel est votre âge " + nom_personne + " ? ")
        try:
            age_int = int(age_int)
            if age_int == 0 :
                print("Votre âge ne peut pas être nul.")
                age_int = 0
        except:
            print("Erreur, vous devez rentrer un nombre entier pour l'âge.")
            age_int = 0
    return age_int

"""
personne = 0

while personne < 8 :
    personne += 1
    print("Personne n°"+ str(personne) )
    nom1 = demander_nom()
    age1 = demander_age(nom1)
    afficher_information_personne(nom1, age1)
"""


"""
# numero_personne()
nom1 = demander_nom()
age1 = demander_age(nom1)
afficher_information_personne(nom1,age1)

# numero_personne()
nom2 = demander_nom()
age2 = demander_age(nom2)
afficher_information_personne(nom2,age2)
"""

NB_PERSONNES = 2

for personne in range(0,NB_PERSONNES) :
    # print("Personne n°" + str(personne+1))
    # nom = demander_nom()
    nom = "Personne "+str(personne+1)
    age = demander_age(nom)
    # taille = int(input("Quelle est votre taille en cm ? "))/100
    afficher_information_personne(nom, age, 1.90)



