import json
personne = {
    "Nom": "Felix Maina",
    "Contact Number": +41792345678,
    "Email": "fely@gmail.com",
    "Amis" : ["Sophie", "Pablo", "Alejandra"]
    }
    

# dictionnaire "personne"
personne_convertie_en_json = json.dumps(personne)
# sérialisation au format json = txt structuré

file = open("fichier_json.txt", "w")
# création d'un fichier (suppression de l'ancien si existant)
file.write(personne_convertie_en_json)
# rédaction du json sérialisé dans ce fichier
file.close()

file = open("fichier_json.txt", "r")
donnees_json = file.read()
# lecture des données du fichier json
file.close()
personne2 = json.loads(donnees_json)
# désérialsation des données depuis le format json
# stockage dans l'objet "personne2"

print(personne2)
# appel et affichage de la clef "Nom" du dictionnaire personne2
# print(personne) # affichage du dictionnaire initial
# print(personne2) # affichage du nouveau dictionnaire
# print(personne == personne2) # test si les 2 dictionnaires sont identiques
print("skdjfdj")