import time

def transformation_temps_en_str(secondes):
    minutes = secondes//60
    secondes = secondes - minutes*60
    min_unit = "minutes"
    sec_unit = "secondes"
    if minutes <= 1 :
        min_unit = "minute"
    if secondes <= 1:
        sec_unit = "seconde"
    r = ""
    if minutes > 0:
        r += f"{minutes} {min_unit}"
    if secondes > 0:
        if len(r) > 0:
            r+= " "
        r+= f"{secondes} {sec_unit}"
    return r

def demande_nombre_entier(valeur_min,valeur_max):
    nombre_entier = input(f"Veuillez saisir un nombre entre {valeur_min} et {valeur_max}. ")
    try :
        nombre_entier_int = int(nombre_entier)
    except:
        print(f"ERREUR : Veuillez saisir un nombre entre {valeur_min} et {valeur_max}")
        return demande_nombre_entier(valeur_min,valeur_max)
    if not( valeur_min <= nombre_entier_int <= valeur_max):
        print(f"ERREUR : Veuillez saisir un nombre entre {valeur_min} et {valeur_max}")
        return demande_nombre_entier(valeur_min, valeur_max)
    print(f"Vous avez choisi {nombre_entier_int}.")
    return nombre_entier_int

DUREE_PROGRESSION = 10

CHOIX_CUISSON = (
    ("Oeufs à la coque", 5),
    ("Oeufs mollets", 6*60),
    ("Oeufs durs", 9*60),
    ("Steack", 5*50),
)

print("Choix de la cuisson")
index_choix = 1
PROPOSITION_MIN = index_choix
PROPOSITION_MAX = len(CHOIX_CUISSON)

for choix_cuisson in CHOIX_CUISSON:
    temps = transformation_temps_en_str(choix_cuisson[1])
    print(f"{index_choix} - {choix_cuisson[0]} : {temps}")
    index_choix +=1

choix = demande_nombre_entier(PROPOSITION_MIN,PROPOSITION_MAX)
choix_cuisson = CHOIX_CUISSON[choix-1]
duree = choix_cuisson[1]

while True:
    print(transformation_temps_en_str(duree), end="", flush=True)
    for i in range(DUREE_PROGRESSION):
        time.sleep(1)
        print(".", end="", flush=True)
        duree -= 1
        if duree == 0:
            break
    print()
    if duree == 0:
        break
print("Le repas est prêt !")




