# utilisateur cherche nombre magique entre 1 et 10 et à 4 vie

import random

NB_MIN = 1
NB_MAX = 10
NB_MAGIQUE = random.randint(NB_MIN,NB_MAX)
NB_VIE = 4
vies = NB_VIE


def nb_test(NB_MIN,NB_MAX) :
    nb_str = input(f"Quel est le nombre magique compris entre {NB_MIN} et {NB_MAX} ? ")
    nb_int = 0
    while nb_int == 0 :
        try :
            nb_int = int(nb_str)
        except :
         print(f"ERREUR : Vous devez saisir un nombre compris entre {NB_MIN} et {NB_MAX}. ")
         nb_str = input(f"Quel est le nombre magique compris entre {NB_MIN} et {NB_MAX} ? ")
        else :
            if NB_MAX < nb_int or nb_int < NB_MIN :
                print(f"ERREUR : Vous devez saisir un nombre compris entre {NB_MIN} et {NB_MAX}. ")
                nb_int = 0
    return nb_int

def control_si_juste(nb_essaye,NB_MAXIQUE) :
    if nb_essaye == NB_MAGIQUE :
        print(f"Bravo, vous avez trouvé le nombre magique {NB_MAGIQUE}.")
    elif nb_essaye < NB_MAGIQUE :
        print("Le nombre est plus petit que le nombre magique.")

    # elif nb_essaye > NB_MAGIQUE:
    #     print("Le nombre est plus grand que le nombre magique.")

    else :
        print("Le nombre est plus grand que le nombre magique.")

nb_essaye = 0

while nb_essaye != NB_MAGIQUE :
    nb_essaye = nb_test(NB_MIN, NB_MAX)
    control_si_juste(nb_essaye,NB_MAGIQUE)

















"""
def nombre_magique_cree(nb_min,nb_max) :
    import random
    nombre_aleatoire = int((random.random()*nb_max)+1)
    while nombre_aleatoire < nb_min :
        nombre_aleatoire = int((random.random()*nb_max)+1)
    print(nombre_aleatoire)
    return nombre_aleatoire


"""
"""
    for i in range (0,100) :
        nombre_magique = int((random.random()*10)+1)
        print(nombre_magique)
"""
"""


def demande_valeur(nombre_magique,nombre_test,nb_min,nb_max) :
    try :
        valeur_test = int(input("Quel est le nombre magique ? "))
    except :
        print(f"Veuillez saisir un nombre entier compris entre {nb_min} et {nb_max}.")
    else :
        if nombre_magique == valeur_test :
            print(f"Bravo, vous avez trouvé le nombre magique qui était {nombre_magique}.")
            return valeur_test
        elif nombre_magique > valeur_test and valeur_test >= nb_min :
            print(f"Le nombre magique est plus grand que {valeur_test}.")
            return valeur_test
        elif nombre_magique < valeur_test and valeur_test <= nb_max :
            print(f"Le nombre magique est plus petit que {valeur_test}.")
            return valeur_test
        else :
            print(f"Veuillez saisir un nombre entier compris entre {nb_min} et {nb_max}.")
            return valeur_test


def nombre_vie(nombre_dessai_restant,nombre_magique,nombre_test) :
    if nombre_test != nombre_magique :
        nombre_dessai_restant -= 1
        return nombre_dessai_restant
    else :
        return nombre_dessai_restant


def test_nombre_vies(nombre_dessai_actuel,nombre_magique,nombre_test):
    if nombre_dessai_actuel == 0 :
        print("Vous avez perdu. Vous avez utilisé toutes vos vies.")
        print(f"Le nombre magique était {nombre_magique}.")
    elif nombre_dessai_actuel > 0 and nombre_magique != nombre_test :
        print(f"Il vous reste {nombre_dessai_actuel} vies.")


nombre_dessai = 4
nb_min = int(input("Quel sera le nombre minimum ? "))
nb_max = int(input("Quel sera le nombre maximum ? "))
nombre_magique = nombre_magique_cree(nb_min,nb_max)
"""
"""
for i in range (0,100) :
    nombre_magique = nombre_magique_cree(nb_min,nb_max)
    # nombre_magique(nb_min,nb_max)
"""
"""

nombre_test = 0

print(f"Vous débutez le jeu avec {nombre_dessai} vies.")


while nombre_dessai > 0 and nombre_test != nombre_magique:
    nombre_test = demande_valeur(nombre_magique,nombre_test,nb_min,nb_max)
    nombre_dessai =nombre_vie(nombre_dessai,nombre_magique,nombre_test)
    # print(nombre_dessai)
    test_nombre_vies(nombre_dessai,nombre_magique,nombre_test)

"""

