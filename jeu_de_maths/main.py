import random
print("Je m'appelle" + "Toto")
NB_MIN = 1
NB_MAX = 10
NB_QUESTION = int(input("À combien de questions souhaitez-vous répondre ? "))

nb_reponse_juste = 0

def poser_questions(NB_MIN,NB_MAX) :
    global nb_reponse_juste
    nb_1 = random.randint(NB_MIN,NB_MAX)
    nb_2 = random.randint(NB_MIN,NB_MAX)
    o = random.randint(0, 2)


    operateur_str = "+"
    reponse_vrai = nb_1 + nb_2
    if o == 1 :
        operateur_str = "-"
        reponse_vrai = nb_1 - nb_2
    elif o == 2 :
        operateur_str = "*"
        reponse_vrai = nb_1 * nb_2
    reponse = input(f"{nb_1} {operateur_str} {nb_2} > Réponse ? ")
    reponse_int = int(reponse)
    if reponse_int == reponse_vrai :
        return True
    return False


for i in range (0,NB_QUESTION):
    print(f"Question n° {i+1}/{NB_QUESTION}")
    if poser_questions(NB_MIN, NB_MAX) :
        nb_reponse_juste +=1
        print("Correct")
    else :
        print("Faux")
    print()

print(f"Votre score est de {nb_reponse_juste}/{NB_QUESTION}.")

#4/4 = Excellent
#0/4 = Révisez vos maths
# Supérieur à la moyenne = int(NBTOT/2)
# SI supérieur moyernne = "Pas mal.
# si inférieur > peut mieux faire.

if nb_reponse_juste == NB_QUESTION :
    print("Excellent")
elif nb_reponse_juste == 0:
    print("Révisez vos maths")
elif nb_reponse_juste > int(NB_QUESTION/2) :
    print("Pas mal.")
else :
    print("Peut mieux faire.")

