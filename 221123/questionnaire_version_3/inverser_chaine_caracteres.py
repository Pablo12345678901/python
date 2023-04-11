"""
def fonction_tri_personnalise_a_creer(element):
	return i


"""
"""
#chaine_caractere = input("Quelle chaîne à inverser ? ")
chaine_caractere = "1234aba1"
#chaine_caractere_inversee = [caractere for caractere in chaine_caractere].sort(reverse=True,key=fonction_tri_personnalise_a_creer)
chaine_caractere_inversee = ["" for caractere in chaine_caractere]
#print(list(chaine_caractere_inversee))
"""
"""
for i in range(len(chaine_caractere_inversee)):
	chaine_caractere_inversee[i] = chaine_caractere[len(chaine_caractere)-1-i]
"""
"""
print("".join(chaine_caractere_inversee))
"""
"""
chaine_caractere = "1234aba1"
chaine_caractere_inversee = chaine_caractere[::-1]
print(chaine_caractere)
print(chaine_caractere_inversee)
"""

"""
def mot_le_plus_long_et_le_plus_cours(str : str):
    liste_mots = str.split()
    mot_le_plus_court = liste_mots[0]
    mot_le_plus_long = liste_mots[0]
    for i in range(len(liste_mots)):
        if len(liste_mots[i])<len(mot_le_plus_court):
            mot_le_plus_court = liste_mots[i]
        if len(liste_mots[i])>len(mot_le_plus_long):
            mot_le_plus_long = liste_mots[i]
    return mot_le_plus_court, mot_le_plus_long
"""
def mot_le_plus_long_et_le_plus_cours(str : str):
    list_word = str.split()
    #print(list(list_word))
    min_word = min(list_word,key=len)
    max_word = max(list_word,key=len)
    return min_word, max_word
"""
def mot_le_plus_long_et_le_plus_cours_sorted(str : str):
    min_word, max_word = mot_le_plus_long_et_le_plus_cours(str)
    min_len, max_len = len(min_word), len(max_word)
    list_word_min = sorted([word for word in str.split() if len(word)==min_len])
    print(list_word_min[0])
    list_word_max = sorted([word for word in str.split() if len(word)==max_len])
    print(list_word_max[0])
"""
def mot_le_plus_long_et_le_plus_cours_sort(str : str):
    list_word = str.split()
    list_word.sort()
    #print(list(list_word))
    min_word = min(list_word,key=len)
    max_word = max(list_word,key=len)
    return min_word, max_word



str = "ab ac ad da ba zz suis Pablo aa j'habite avenue Pictet de Rochemont"
min_word, max_word = mot_le_plus_long_et_le_plus_cours(str)
mot_le_plus_long_et_le_plus_cours_sort(str)
print(f"Mot le plus court = {min_word}")
print(f"Mot le plus long = {max_word}")
