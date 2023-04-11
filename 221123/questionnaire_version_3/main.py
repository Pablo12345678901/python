import json
# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

"""
# class
    attributs
    actions

class question
    attributs :
        titre : str
        choix : [str]
        réponse : str
    actions :
        poser question -> boolean
            demander_reponse : str

class questionnaire
    attributs :
        liste questions : list(Questions)
    actions :
        lancer questionnaire
        gestion du sore
"""

class Question():
    def __init__(self, titre : str, choix : [str], reponse : str):   
        self.titre = titre
        self.choix = choix
        self.reponse = reponse

    def FromData(data):
        q = Question(data[2], data[0], data[1])
        return q
        
    def poser(self):
        # titre_question, r1, r2, r3, r4, choix_bonne_reponse
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = self.demander_reponse_numerique_utlisateur()
        if self.choix[reponse_int-1].lower() == self.reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    
    def demander_reponse_numerique_utlisateur(self):
        reponse_str = input("Votre réponse (entre 1 et " + str(len(self.choix)) + ") :")
        try:
            reponse_int = int(reponse_str)
            if 1 <= reponse_int <= len(self.choix):
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return demander_reponse_numerique_utlisateur(min, max)

class Questionnaire():
    def __init__(self, liste_question : [object]):   
        self.liste_question = liste_question
        #self.lancer()
    
    def lancer(self):
        score = 0
        for question in self.liste_question:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.liste_question))
        return score

'''
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
'''



'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''



"""
questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)
"""
data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris","Quelle est la capitale de la France ?")
q = Question.FromData(data)


liste_questions = [
    q,
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles"),
    ]

print(liste_questions[1].__dict__)

"""
#a = Questionnaire(liste_questions).lancer()
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

a = Questionnaire(liste_questions)
jsonString = json.dumps(q)
print(jsonString)
"""

