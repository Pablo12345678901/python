"""
noms = ["Marc", "Jean", "Marie", "Pablo", "Alain", "Ziad"]
nom_check = ["Marie", "Josiane"]
nombres = [1, 2, 3, 4, 6, 7, 8, 0]

# print(noms.index("Marc", 3))

valeur_recherchee = input("Quelle est la valeur recherchée ? ")

nb_occurences = noms.count(valeur_recherchee)
print("nb_occurences = ", nb_occurences)
if nb_occurences > 0:
    debut_intervalle = 0
    for i in range(nb_occurences):
        index = noms.index(valeur_recherchee, debut_intervalle)
        print(valeur_recherchee, "trouvé à l'index :", index)
        debut_intervalle = index + 1
else:
    print("L'élément n'est pas dans la collection.")
"""
'''
noms = ["Ma", "Jea", "Marie", "Pablo", "Alain-Thierry", "Ziad abdelwahed"]
longueur_noms = [(True if len(nom) > 4 else False)  for nom in noms]
print(longueur_noms)
'''



"""
# test = any(longueur_noms)
# print("Le résultat est", test)
string_a_tester = "Mohamed"
list_a_tester = [True if char.isdigit() else False for char in string_a_tester]
# print(list_a_tester)
tester_si_nombre_dans_string = any(list_a_tester)
print("Est-il vrai que ce string contient un/des nombre(s) ? ",tester_si_nombre_dans_string)
"""
nom = ""
while nom == "":
    nom = input("Quel est ton nom ? ")
    if nom == "":
        print("ERREUR : Le nom est vide.")
    elif any([char.isdigit() for char in nom]):
        print("ERREUR : Ce nom contient un/des nombres.")
        nom = ""
    elif not (nom.replace(" ", "") == nom):
        nom = nom.replace(" ", "")
        print("ERREUR : Ce nom contient un/des espaces.")
        print(f"Voulez-vous dire :'{nom}' ?")
        test = input("Si oui, faites entrée. Sinon, tapez autre chose.")
        if test == "":
            print("Votre nom est :", nom)
            break
        else:
            print("Vous avez choisi de re-saisir votre nom.")
            nom = ""
    else:
        print("Votre nom est :", nom)
        break
    print("Veuillez resaisir votre nom.")











