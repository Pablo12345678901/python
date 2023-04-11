class Chat:
    def __init__(self, nom=""):
        if nom == "":
            nom = "inconnu"
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis un chat et je m'appelle " + self.nom)


chat1 = Chat()
chat1.SePresenter()

str = "installer des packages sur PyCharm"
print(str.upper())