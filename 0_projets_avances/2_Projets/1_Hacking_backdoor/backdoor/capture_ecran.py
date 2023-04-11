#IMPORT BIBLIOTHEQUE ET FONCTION 
from PIL import ImageGrab

#PRENDRE UNE CAPTURE D'ECRAN AVEC GRAB
capture_ecran = ImageGrab.grab()

#AFFICHER LA CAPTURE D'ECRAN AVEC SHOW
#capture_ecran.show()

#SAUVEGARDE DE LA CAPTURE D'ECRAN
capture_ecran.save("capture1.png", "PNG")
# paramètres :
#   nom
#   format en majuscule
# recommandation d'utiliser le PNG car c'est un format compressé
# et il fonctionne sur tous les systèmes 
# Il est important de se placer dans le bon répertoire avant de sauver

#TESTER SI LE NOM DU FICHIER CONTIENT L'EXTENSION ET LA RAJOUTER SINON
# En faisant le check de :
# si le nom du fichier contient l'extension, ne pas le rajouter
#ICI EXEMPLE AVEC PLUSIEURS NOM DE FICHIER
liste_nom_fichiers = ["babe", "babe.jpg", "bab.ejpg", "babe.png", "png.babe"]
for i in range (len(liste_nom_fichiers)):
    #nom_du_fichier = "babe"
    if len(liste_nom_fichiers[i].split(".")) == 1:
        liste_nom_fichiers[i] += ".png"
    else:
        liste = liste_nom_fichiers[i].split(".")
        print(liste)
        liste_extensions = ["png", "jpg"]
        if not liste[-1] in liste_extensions:
            liste_nom_fichiers[i] += ".png"
for each in liste_nom_fichiers:
    print(each)
# sinon, rajouter l'extension "".png"