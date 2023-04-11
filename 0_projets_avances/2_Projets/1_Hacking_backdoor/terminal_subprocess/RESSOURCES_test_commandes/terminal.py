import subprocess
import os
while True:
    commande = input(os.getcwd() + " > ")
    if commande == "exit":
        break
    commande_split = commande.split(" ")
    # séparation de la commande en morceaux - grâce aux espaces
    if len(commande_split) == 2 and commande_split[0] == "cd":
        # la commande cd a une longueur d'exactement 2 et son premier paramtères est "cd"
        # si c'est le cas (des 2 conditions):
        try:
            os.chdir(commande_split[1])
            # on essaye de change de répertoire avec le deuxième paramètres
        except FileNotFoundError:
            print(f"ERREUR : le répertoire {commande_split[1]} n'est pas valide.")
            # sinon on affiche un message d'erreur
    else:
        resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)
        if resultat.returncode == 0:
            print(f"Résultat : \n{resultat.stdout}")
        else:
            print(f"Message d'erreur : \n{resultat.stderr}")
