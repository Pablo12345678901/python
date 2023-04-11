import copy

class Personne:
    TYPE = 0
    def __init__(self, nom : str, age : int, list : list):
        self.nom = nom
        self.age = age
        self.list = list
        while not isinstance(self.age, int):
            try:
                self.age = int(input("Quel est votre âge ? "))
            except:
                print("Veuillez saisir un nombre entier > 0.")
            
    def __repr__(self):
        return "FDP"
    
    @staticmethod
    def formater_chaine(a):
        return a[0].upper() + a[1:].lower()
    
    @classmethod
    def methode_de_classe(cls):
	    print("Méthode de classe :", cls.TYPE)
                
    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}.")
        print(f"L'an prochain, j'aurai {self.age+1} ans.")
        print(f"{self.list}.")


"""
    def __eq__(self,other):
        return self.nom == other.nom and self.age == other.age
"""       
    
personne1 = Personne("Pablo", 26, [1, 2, 3, 4])
#personne1.AfficherInfos()
#print(personne1)
print(personne1.formater_chaine("jeaN"))
Personne.methode_de_classe()
"""
personne2 = personne1
personne2 = copy.deepcopy(personne1)
print("personnne1 : ", personne1.__dict__)
print("personnne2 : ", personne2.__dict__)
print("modif personne1")
personne1.nom = "PD"
personne1.list[0] = 5
print("personnne1 : ", personne1.__dict__)
print("personnne2 : ", personne2.__dict__)
print("Test == : ", personne1 == personne2)
print("Test is : ",personne1 is personne2)
"""

"""
personne2 = Personne("Pablo", 20)
personne2.AfficherInfos()
"""


#print(personne1.__dict__ == personne2.__dict__)
