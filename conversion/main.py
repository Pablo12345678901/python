# 1 pouce = 2.54 cm
# 1 cm = 0.394 pouces

# Voici comment votre programme doit se comporter :
# 1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
# 2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
# 3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
# - fin du programme.

# 1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"


def type_de_conversion() :
    type_conversion_int = 0
    while type_conversion_int == 0 :
        type_conversion = input("Souhaitez-vous convertir de : 1 = pouces vers cm ou 2 = cm vers pouces ? Tapez 1 ou 2 selon votre choix. ")
        print()
        try :
            type_conversion_int = int(type_conversion)
        except :
            print("ERREUR : Vous n'avez pas saisi 1 ou 2.")
            print()
        if 0 > type_conversion_int or type_conversion_int > 2 :
            print("ERREUR : Vous n'avez pas saisi 1 ou 2.")
            print()
            type_conversion_int = 0
    if type_conversion_int == 1 :
        print("Vous avez choisi de converti des pouce(s) en cm.")
        print()
    else :
        print("Vous avez choisi de converti des cm en pouce(s).")
        print()
    return type_conversion_int


def demande_valeur ():
    valeur_a_convertir_float = 0.0
    while valeur_a_convertir_float == 0.0:
        valeur_a_convertir = input("Quel valeur souhaitez-vous convertir ? ")
        print()
        try:
            valeur_a_convertir_float = float(valeur_a_convertir)
            if valeur_a_convertir_float == 0:
                print("ERREUR : Vous avez saisi le nombre 0.0.")
                print()
        except:
            print("ERREUR : Vous n'avez pas saisi un nombre.")
            print()
            valeur_a_convertir_float = 0.0
    return valeur_a_convertir_float


def conversion(type,valeur) :
    if type == 1 :
        valeur_convertie = round((valeur * 2.54),2)
        print(f"{valeur} pouce(s) font {valeur_convertie} cm.")
        print()
    else :
        valeur_convertie = round((valeur * 0.394),2)
        print(f"{valeur} cm font {valeur_convertie} pouce(s).")
        print()
    return valeur_convertie


def continuer_conversion():
    demande = input("Souhaitez-vous continuer ? Pour arrêter, tapez 1. Sinon, tapez autre chose. ")
    print()
    if demande != "1" :
        print("Vous avez choisi de continuer les conversions.")
        print()
        return True
    return False


type = type_de_conversion()
continuer = True


while continuer :
    valeur = demande_valeur()
    valeur_convertie = conversion(type, valeur)
    continuer = continuer_conversion()
print("Vous avez choisi d'arrêter les conversions.")
