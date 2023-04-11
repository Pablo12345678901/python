#Questionnaire
"""
Affichage question
Affichage réponse (a,b,c,d,...)
Demande réponse
Comparaison réponse avec réponse véritable
Affichage message Bonne / mauvaise réponse
Question suivante
"""

#"""
#exercice amélioré
questions_et_reponses = (
	{
		"question": "Quelle est la capitale de la France ? ",
		"reponse": "Paris",
	},
    	{
		"question": "Quelle est la capitale de l'Italie ? ",
		"reponse": "Rome",
	},
    {
		"question": "Quelle est la capitale de la Suisse ? ",
		"reponse": "Berne",
	},
)

liste_reponses_proposees = (
    ("Marseille", "Nice","Paris","Nantes"),
    ("Rome", "Venise","Milan","Turin", "Naples"),
    ("Lausanne", "Genève","Berne","Uri", "Schwitz", "Renens", "Meyrin"),
)

nb_bonnes_reponses = 0

for i in range(len(questions_et_reponses)):
    print("Question :", questions_et_reponses[i]["question"])
    lettre_reponse = 'a'
    for q in range(len(liste_reponses_proposees[i])):
        print("("+ lettre_reponse+")", liste_reponses_proposees[i][q])
        lettre_reponse = chr(ord(lettre_reponse)+1)

    reponse_utilisateur = input("\nQuelle est votre réponse ? ")
    # besoin fonction conversion
    reponse_utilisateur_en_int = ord(reponse_utilisateur)-96
    if questions_et_reponses[i]["reponse"]== liste_reponses_proposees[i][reponse_utilisateur_en_int-1]:
        print("\nBonne réponse\n")
        nb_bonnes_reponses += 1
    else :
        print("\nMauvaise réponse\n")
unit = "bonne réponse"
if nb_bonnes_reponses > 1:
    unit = "bonnes réponses"

print("Fin du questionnaire. Vous avez fait un score de", nb_bonnes_reponses, unit + ".")
#"""




"""
#exercice de base
print("Question : Quelle est la capitale de la France ? ")
print("(a) Marseille")
print("(b) Nice")
print("(c) Paris")
print("(d) Nantes")
reponse_utilisateur = input("Quelle est votre réponse ? ")
if reponse_utilisateur == reponse_question:
    print("Bonne réponse")
else :
    print("Mauvaise réponse")


"""
