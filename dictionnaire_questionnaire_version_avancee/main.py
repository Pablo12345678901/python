"""
questionnaire=[
             {
                "titre": "",
                "reponses": ("", "", "", ""),
                "bonne_reponse": "2"
             },
            {
                "titre": "",
                "reponses": ("", "", "", ""),
                "bonne_reponse": "2"
             },
            {
                "titre": "",
                "reponses": ("", "", "", ""),
                "bonne_reponse": "2"
             },


]
"""
def demander_choix(tuple : tuple) -> str:
    # définition de la gamme des réponses (lettres admises)
    gamme_reponse = []
    for i in range(len(tuple)):
        lettre = chr(i + 96 + 1)
        gamme_reponse += lettre
    #print(gamme_reponse)
    choix = input("\nVotre réponse ? ")
    if choix.lower() in gamme_reponse:
        return choix.lower()
    print("\nErreur : vous devez saisir une valeur comprise entre", gamme_reponse[0], "et", gamme_reponse[-1])
    return demander_choix(tuple)

def poser(tuple : tuple) -> bool:
    # global score
    print(tuple[0])
    print("\nListe de choix :")
    lettre = "a"
    for element in tuple[1]:
        print(lettre, element)
        lettre = chr(ord(lettre)+1)
    reponse_str = demander_choix(tuple[1])
#    print(reponse_str)
    reponse_int = (ord(reponse_str) - 96) - 1
#    print(reponse_int)
    bonne_reponse = False
    if tuple[1][reponse_int] == tuple[2]:
        print("\nBonne réponse\n")
        bonne_reponse = True
        # score += 1
    else:
        print("\nMauvaise réponse\n")
    return bonne_reponse

#"""
def creer_question() -> tuple:
    question = []
    question.append(input("Quelle question souhaitez-vous poser ? "))
    # print(question)
    reponse_proposees = input("Quelle sera la liste des réponses ? Veuillez les séparer par des virgules. ")
    reponse_proposees_tuple = reponse_proposees.replace(" ", "").split(",")
    # print(reponse_proposees_tuple)
    question.append(reponse_proposees_tuple)
    # print(question)
    reponse_question = input("Quelle sera la réponse à la question ? ").replace(" ", "")
    while not (reponse_question in question[1]):
        print("Erreur : cette réponse ne fait pas partie des réponses de la liste. ")
        reponse_question = input("Quelle sera la réponse à la question ? ").replace(" ", "")
    question.append(reponse_question)
    # print(question)
    return question

def questionnaire(tuple : tuple)-> None:
    unit = "bonne réponse"
    score = 0
    for chaque_question in tuple:
        if poser(chaque_question):
            score += 1

    if score > 1:
        unit = "bonnes réponses"

    print(f"\nScore final = {score}/{len(tuple)} {unit}.")
#"""



#""" Version intermédiaire avec questionnaire automatique - pas d'auto-création de question

question1 = ("\nQuelle est la capitale de la France ?", ("Paris", "Toulouse", "Bordeaux", "Ferney"), "Paris")
question2 = ("\nQuelle est la capitale de l'Italie ?", ("Milan", "Turin", "Rome", "Venise", "Toronto"), "Rome")
liste_questions = [question1, question2]

questionnaire(liste_questions)

#"""




""" Version ultra-avancée avec auto-création de question - puis questionnaire
liste_questions = []
score = 0
unit = "bonne réponse"

while True:
    liste_questions.append(creer_question())
    continuer = input("Voulez-vous faire une autre question ? Si non, tapez entrée, si oui, tapez autre chose, puis entrée.")
    if continuer == "":
        break

questionnaire(liste_questions)
"""
