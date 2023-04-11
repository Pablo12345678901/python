import os
os.chdir('/Users/alejandramt/Desktop')


lines = ['Readme', 'How to write text files in Python']
lines_add = ['===', 'those below lines', 'were not', 'there before.']
try:
    open('readme.txt', 'r')
    # test si le fichier existe
except:
    open('readme.txt', 'x')
    # le crée sinon
with open('readme.txt', 'w') as f:
    # mode rédaction au sein du fichier
    f.writelines("\n".join(lines))
    # rédaction du fichier
f.close()
# fermeture du fichier après l'avoir modifié pour s'assurer de la sauvegarde
with open('readme.txt', 'r') as f:
    # mode lecture du fichier
    Lines = f.readlines()
    # création d'un liste à partir du fichier
    print("Fichier initial")
    for line in Lines:
        print(line.strip("\n"))
        # affichage de chaque ligne du fichier sans le retour à la ligne (sinon à double)
    print()
with open('readme.txt', 'a') as f:
    # mode ajout au sein du fichier
    f.write("\n")
    # retour à la ligne pour éviter que la fin de la première liste soit collé au début de la 2ème
    f.writelines("\n".join(lines_add))
    # rédaction du fichier
f.close()
# fermeture du fichier après l'avoir modifié pour s'assurer de la sauvegarde
with open('readme.txt', 'r') as f:
    print("Fichier augmenté")
    # mode lecture du fichier
    Lines = f.readlines()
    # création d'un liste à partir du fichier
    for line in Lines:
        print(line.strip("\n"))
        # affichage de chaque ligne du fichier sans le retour à la ligne (sinon à double)
    print()
