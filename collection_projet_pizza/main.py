"""
menu = []
while True:
    pizza = input("Pizza à ajouter au menu : ")
    if pizza == "":
        break
    menu.append(pizza)
    menu.sort()
print("Menu")
for each_pizzas in menu:
    print(each_pizzas)
print("Bon appétit")
"""

def fonction_tri_personnalise_a_creer(element):
	return len(element)

def afficher(collection : tuple, nombre=-1) -> None:
#       collection.sort(reverse=False, key=fonction_tri_personnalise_a_creer)
        # collection.sort()
        if not (nombre == -1):
            collection = collection[0:nombre]
        if len(collection) == 0:
            print("AUCUNE PIZZA")
        else:
            nb_tiret = 4
            if nombre == -1:
                nombre = len(collection)
            print(nb_tiret*"-", "LISTE DES PIZZA ("+ str(min(len(collection),nombre)) + ")", nb_tiret*"-")
            for each_element in collection[:nombre]:
                print(each_element)
            print()
            print("Première pizza :", collection[0])
            print()
            print("Première pizza :", collection[-1])

def ajouter_pizza_utilisateur(collection : tuple) -> None:
    while True:
        nouvelle_pizza = input("Pizza à ajouter : ")
        if nouvelle_pizza == "":
            break
        nouvelle_pizza = nouvelle_pizza.lower()
        if nouvelle_pizza in collection:
            print("Erreur, cette pizza existe déjà")
        else:
            collection.append(nouvelle_pizza)

def pizza_existe(e, collection) -> bool:
    for i in collection:
        if e == i:
            return True
    return False


pizza = ["4 fromages", "végétarienne", "hawaï", "calzone"]
#pizza = []
ajouter_pizza_utilisateur(pizza)
afficher(pizza, 7)
