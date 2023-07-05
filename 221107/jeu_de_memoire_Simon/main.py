import os
import time
import random
#
# fonction de nettoyage d'écran
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
#
# collection des niveaux de difficultés
"""
NIVEAU_DIFFICULTE = (
    ("facile", 4, 3, 1), #( longueur chaîne de caractères initiale, temps d'affichage de la chaîne, ajout du nombre de caractère supplémentaire)
    ("intermédiaire", 6, 2, 2),
    ("difficile", 8, 1, 3),
    )
"""
NIVEAU_DIFFICULTE = (
	{
		"titre": "Facile",
		"longueur_initiale": 4,
		"duree_memorisation": 3,
		"increment_sequence" : 1,
	},
# 1er niveau du dictionnaire
	{
		"titre": "Moyen",
		"longueur_initiale": 6,
		"duree_memorisation": 2,
		"increment_sequence" : 3,
	},
# 2ème niveau du dictionnaire (...)
	)





"""
# affichage des niveau de difficultés
for niveau_difficulte in NIVEAU_DIFFICULTE:
    #print(niveau_difficulte[0])
    print(f"{i} niveau {niveau_difficulte[0]}")
    i += 1
"""
for i in range(len(NIVEAU_DIFFICULTE)) :
    #print(niveau_difficulte[0])
    word = NIVEAU_DIFFICULTE[i]["titre"]
    print(f"{i+1} niveau {word}")

niveau_max = len(NIVEAU_DIFFICULTE)

# demande du choix de la difficulté
while True :
    choix_difficulte = input(f"Choix niveau difficulté entre {1} et {niveau_max}. ")
    try :
        choix_difficulte_int = int(choix_difficulte)
    except :
        print(f"ERREUR : Vous devez faire un choix du niveau difficulté entre {1} et {niveau_max}. ")
    else :
        if not (1 <= choix_difficulte_int <= niveau_max) :
            print(f"ERREUR : Vous devez faire un choix du niveau difficulté entre {1} et {niveau_max}. ")
        else :
            choix_difficulte_int -=1
            break
word1 = NIVEAU_DIFFICULTE[choix_difficulte_int]["longueur_initiale"]
word2 = NIVEAU_DIFFICULTE[choix_difficulte_int]["duree_memorisation"]
word3 = NIVEAU_DIFFICULTE[choix_difficulte_int]["increment_sequence"]
print(f"Vous avez choisi les paramètres suivants :\nLongueur de chaîne de caractères initiale : {word1}\ntemps d'affichage de la chaîne : {word2}\najout du nombre de caractère supplémentaire : {word3}")


# 0 - Générer une chaine de caractère qui contient 4 chiffres aléatoires, c'est votre séquence initiale.

score = 0
n = ""
#n = str(random.randint(0, 9))
longueur_nb_initiale = NIVEAU_DIFFICULTE[choix_difficulte_int]["longueur_initiale"]
temps_d_affichage = NIVEAU_DIFFICULTE[choix_difficulte_int]["duree_memorisation"]
for i in range (longueur_nb_initiale):
    n+= str(random.randint(0, 9))
    # print(n) # debug

#mise au singulier de l'unité seconde si le temps d'affichage est <= à 1
sec_unit = "secondes"
word4 = NIVEAU_DIFFICULTE[choix_difficulte_int]["duree_memorisation"]
if word4 <= 1:
    sec_unit = "seconde"

#Descriptif du jeu
word5 = NIVEAU_DIFFICULTE[choix_difficulte_int]["duree_memorisation"]
print(f"\nCeci est un jeu de mémoire.\nVous allez devoir retenir une séquence de nombres de plus en plus longue.\nElle s'affichera et disparaîtra de votre écran après {word5} {sec_unit}.\n")
time.sleep(2)


# 1 - Ajouter un nouveau nombre aléatoire à la fin de votre séquence
while True:
    #n+= (NIVEAU_DIFFICULTE[choix_difficulte_int][3])*str(random.randint(0, 9))
    # print(n) # debug

    # 2 - Nettoyer l'écran et affichez "Retenez la séquence" pendant 1 seconde
    
    print("\nRetenez la séquence\n")
    time.sleep(1)

    # 3 - Afficher la séquence à mémoriser pendant 3 secondes
    print(f"{n}\n")
    time.sleep(temps_d_affichage)

    # 4 - Nettoyer n'écran et demander la réponse à l'utilisateur
    
    clear_screen()
    print(n) #debug
    reponse = input("Quelle est la séquence ? ")

    # 5 - Si la réponse est bonne, afficher pendant 1 seconde "Bonne réponse, votre score est : xxx", puis reboucler à l'étape 1
    if reponse == n :
        score +=1
        print(f"\nBonne réponse, votre score est : {score}\n")
        time.sleep(1)
        n+= (NIVEAU_DIFFICULTE[choix_difficulte_int]["increment_sequence"])*str(random.randint(0, 9))

    # 5bis - Si la réponse n'est pas bonne, sortir du programme et afficher : "Mauvaise réponse, la séquence était : xxxx, votre score final : xxxx"
    else :
        print(f"\nVotre réponse : {reponse}")
        break
print(f"\nMauvaise réponse, la séquence était : {n}, votre score final : {score}\n")
print("Fin du programme\n")