import requests
# besoin de ce module pour faire des requête http
import json
# module utile pour les désérialisation
url = "https://comptedemoettests.pythonanywhere.com/api/GetPizzas"
#RÉCUPÉRATION DES DONNÉES DANS UNE VARIABLE
data = requests.get(url)
#MONTRER QUEL EST L'ENCONDEUR DE LA PAGE
#DEBUG print(data.encoding)
#MODIFIER L'ENCODEUR A UTF-8 POUR GERER LES ACCENTS
data.encoding = "utf-8"
#DESERIALISATION DES DONNEES
pizzas = json.loads(data.text)
#DEBUG print(pizzas)
#AFFICHAGE DES DONNEES
# c'est un tableau utilisable par Python
print(str(len(pizzas))+" objets dans le tableau Python")
for pizzaModel in pizzas:
    pizza = pizzaModel["fields"]
    # récupération du champ 'fields' uniquement et pas des autres champs produits par django
    print(pizza['nom'] + " : " +str(pizza['prix']))
    print(pizza['ingredients'])
    print()

str = "GIT TUTORIEL POUR GESTION DE PROJETS"
print(str.lower())

