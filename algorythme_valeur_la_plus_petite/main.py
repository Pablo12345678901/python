from operator import itemgetter
"""

nom_chauffeur = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

if not (len(nom_chauffeur) == len(distance_chauffeur_km)):
    print("Les listes n'ont pas la même taille. Il y a", len(nom_chauffeur), "chauffeurs et", len(distance_chauffeur_km), "distances.")

"""

"""
distance_chauffeur_km.sort()
distance_min = distance_chauffeur_km[0]
print(distance_min)
"""

"""
index_min = 0
distance_min = distance_chauffeur_km[0]

for i in range(len(distance_chauffeur_km)):
    if distance_chauffeur_km[i] < distance_min:
        distance_min = distance_chauffeur_km[i]
        index_min = i

print("Distance minimale :", distance_min, "km.")
print("Index de la distance minimale:", index_min)
print("Chauffeur à la distance minimale:", nom_chauffeur[index_min])
"""



nom_et_distance_chauffeur = [
    ("Patrick", 1.5, "Paris"),
    ("Paul", 2.2, "Paris"),
    ("Marc", 0.4, "Paris"),
    ("Jean", 0.9,"Dubaï"),
    ("Pierre", 7.1,"Berne"),
    ("Marie", 1.1,"Washington"),
    ("Maxime", 0.6, "Santiago"),
                            ]

nom_et_distance_chauffeur.sort(key=lambda a: a[2])

print(nom_et_distance_chauffeur)
print(itemgetter(1)(nom_et_distance_chauffeur))