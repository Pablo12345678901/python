# demander le nom
def demander_nom():
    nom = input("Quel est votre nom ? ")
    while nom == "":
        nom = input("Veuillez saisir votre nom.")
    return nom


# demander l'âge
def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre âge ? ")
        try:
            age_int = int(age_str)
        except:
            print("Erreur, vous devez rentrer un nombre entier pour l'âge.")
    print("Vous avez " + str(age_int) + " ans.")
    print("L'an prochain, vous aurez " + str(age_int + 1) + " ans.")
    return age_int


nom = demander_nom()
age = demander_age()

print("En résumé, vous vous appelez " + nom + " et avez " + str(age) + " ans.")
