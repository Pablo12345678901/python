import random

"""
def generate_random_list(n, min, max):
    list = []
    for i in range(n):
        list.append(random.randint(min, max))
    list.sort()
    print(list)
    return list
"""
"""
def generate_random_list(n, min, max):
    list = [random.randint(min, max) for each in range(n)].sort()
    print(list)
    return list

liste = generate_random_list(1,1,9)
"""
"""
liste = generate_random_list(100,1,9)
#liste = [10, 9, 2, 3]
for unsorted_index in range(0,len(liste)-1):
    # pour tous les index de la list (sauf le dernier car pas de permutation possible)
    min = liste[unsorted_index]
    # le minimum est représenté par dont la l'élément à l'index dont la liste n'est pas encore triée après
    min_index = unsorted_index
    # l'index minimum est représenté par l'index dont la liste n'est pas encore triée après
    for i in range(unsorted_index+1,len(liste)):
    # pour tous les index de "l'index pas trié +1" à n
        if liste[i] < min:
            # si l'élément est plus petit que le min actuel
            min = liste[i]
            # le min actuel devient l'élément
            min_index = i
            # l'index de l'élément min est i (ci-dessus)
            # échange des 2 index ci-dessous
    liste[min_index] = liste[unsorted_index]
            # finalement, parmi tous les éléments qui ont été filtré
            # écrasement de l'index avec la valeur min 
    liste[unsorted_index] = min
            # remplacement de la valeur dans l'index unsorted
#print(liste)
"""


