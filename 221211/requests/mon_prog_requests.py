#RECUPERATION ET SAUVEGARDE D'UNE IMAGE
# L'image n'est pas un texte, c'est un format binaire
# Toutefois, le fonctionnement est similaire.
import requests
reponse = requests.get("https://codeavecjonathan.com/res/papillon.jpg")
if reponse.status_code == 200:
    # CREATION D'UN FICHIER JPG
    f = open("papillon.jpg", "wb")
    # en mode écriture + binaire = "wb"
    # RECUPERER LE CONTENU AU FORMAT BINAIRE AVEC CONTENT
    f.write(reponse.content)
    # rédiger le contenu du fichier depuis reponse.content = en binaire
    f.close()
    # fermeture du fichier - possible d'éviter avec le "with ... as ..."
    print("Écriture terminée")
    # auto-check pour moi - cela m'indiquera quand ce sera terminé
else:
    print("ERREUR code : "+str(reponse.status_code))