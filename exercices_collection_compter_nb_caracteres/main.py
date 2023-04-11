# compter nb total caractère contenu dans ts les string d'une liste

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

chiffres = [noms.index(nom) for nom in noms]
#print(chiffres)

a = list(zip(noms, chiffres))
# iterator1, iterator2, iterator3 ... : Iterator objects that will be joined together
print(a)


name, numbers = list(zip(*a))
print(name)
print(numbers)
#name = list(name)
# print(name)
# print(numbers)

a = [1, 2, 3]
b = [4, 5, 6]

c = a.extend(b)
print(c)
print(a)

# 1 - avec for et len
"""
nb_caracteres = 0
for i in range(len(noms)):
    # print(len(noms[i]))
    nb_caracteres += len(noms[i])
print("nb_caracteres", nb_caracteres)
"""

# 2 - completion de liste + sum
"""
nb_caracteres_list = [len(nom) for nom in noms]
print(nb_caracteres_list)
print("nb_caracteres", sum(nb_caracteres_list))
"""

# 3 - join / len
"""
total = "".join(noms)
print("nb_caracteres",len(total))
"""