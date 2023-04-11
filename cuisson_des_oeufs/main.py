import time


# fonction qui montre le temps s'écouler et indique le temps restant
def decompte_du_temps_restant(NB_SECONDE_PAR_AFFICHAGE,duree_restante):
    if not NB_SECONDE_PAR_AFFICHAGE > duree_restante :
        for i in range(NB_SECONDE_PAR_AFFICHAGE):
            time.sleep(1)
            print(".", end="", flush=True)
        print("")
        duree_restante -= NB_SECONDE_PAR_AFFICHAGE
    else :
        for i in range(duree_restante):
            time.sleep(1)
            print(".", end="", flush=True)
        print("")
        duree_restante -= duree_restante
    return duree_restante


#demande du choix du durée à l'utilisateur
while True :
    choix = input("""Choissisez la durée selon le type de cuisson :
1 - Oeufs à la coque : 3 minutes
2 - Oeufs mollets : 6 minutes
3 - Oeufs durs : 9 minutes
Veuillez choisir votre durée en tapant 1, 2 ou 3. """)
    print()
    if (choix == "1" or choix == "2" or choix == "3"):
        break
    print("Erreur : veuillez saisir 1, 2 ou 3.\n")


#Début du programme
DUREE = 60*int(choix)*3
NB_SECONDE_PAR_AFFICHAGE = 10
nombre_d_affichage = DUREE/NB_SECONDE_PAR_AFFICHAGE
duree_restante = DUREE

print("Cuisson en cours", end="")
duree_restante = decompte_du_temps_restant(NB_SECONDE_PAR_AFFICHAGE,duree_restante)

while duree_restante > 0:
    nb_minutes = duree_restante // 60
    seconde = duree_restante - (nb_minutes * 60)
    print(f"Durée restante : {nb_minutes:02d}:{seconde:02d}", end="")
    duree_restante = decompte_du_temps_restant(NB_SECONDE_PAR_AFFICHAGE, duree_restante)
print("\nCuisson terminée !\n")

print("Fin du programme")
