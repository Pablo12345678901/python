import random
def generate_random_list(n, min, max):
    list = []
    for i in range(n):
        list.append(random.randint(min, max))
    #list.sort()
    #print(list)
    return list


ages = [1, 15, 2, 6, 18]
for i in range(len(ages)-1, 0, -1):
  # range depuis "l'index max -1" (car l'index du premier élément est 0) jusqu'à l'index 0 à reculons
  # possible remplacer le 0 par 1 car de toute façon pas de permutation pour le dernier élément seul
  # le i est utilisé ci-dessous pour que le tri s'applique sur un intervalle de 0 à i, i étant plus petit de 1 à chaque boucle
  for j in range(0, i):
    if ages[j+1] < ages[j]:
      # Echanger les deux valeurs
      min = ages[j+1]
      # conservation de la valeur min entre les 2 dans la variable min
      ages[j+1] = ages[j]
      # remplacement de la valeur ages[j] par la valeur ages[j+1]
      ages[j] = min
      # remplacement de la valeur ages[j] par la valeur min
print(ages)
