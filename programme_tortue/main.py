import turtle

t = turtle.Turtle()

# instruction : forward = avant / backward = arrière / right = rotation avec angle / left = idem

#exercice 5 marches de 30px

def carre(taille) :
    for i in range (0,4) :
        t.forward(taille)
        t.left(90)

def carres(taille_depart,nb) :
    for i in range (0,nb) :
        taille = (i+1)*(i+1)*taille_depart
        carre(taille)

carres(10,5)




turtle.done()

"""
def nombredemarche(nb,cote_fonction,angle_fonction) :
        for i in range(0, nb_cote) :
            t.forward(cote_fonction)
            t.left(angle_fonction)
"""

"""
def escalier(taille,nb) :
    for i in range(0, nb) :
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)

taille_demandee = int(input("Quelle hauteur de marche ? "))
nb_demande = int(input("Quelle nombre de marche ? "))
escalier(taille_demandee,nb_demande)
"""

"""
nb_cote = int(input("Combien de côté ? "))
cote = int(input("Quel longueur par côté ? "))
angle = 360/nb_cote
nombredemarche(nb_cote,cote,angle)
"""



"""
# drapeau suisse
distance_cote = 75
longueur_pointe = 100
angle_de_rotation = 90

# dessin d'une des 4 pointes
t.forward(longueur_pointe)
t.left(angle_de_rotation)
t.forward(distance_cote)
t.left(angle_de_rotation)
t.forward(longueur_pointe)
t.right(angle_de_rotation)

t.forward(longueur_pointe)
t.left(angle_de_rotation)
t.forward(distance_cote)
t.left(angle_de_rotation)
t.forward(longueur_pointe)
t.right(angle_de_rotation)

t.forward(longueur_pointe)
t.left(angle_de_rotation)
t.forward(distance_cote)
t.left(angle_de_rotation)
t.forward(longueur_pointe)
t.right(angle_de_rotation)

t.forward(longueur_pointe)
t.left(angle_de_rotation)
t.forward(distance_cote)
t.left(angle_de_rotation)
t.forward(longueur_pointe)
t.right(angle_de_rotation)
"""
