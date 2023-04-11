import sys

"""
# utilisation de la récursion simple
def a(n, limit) -> None:
    print("n :", n)
    if n > limit:
        return
    a(n*n, limit)

a(3, 10000000000000)
"""



"""
# utilisation de la récursion avec renvoi de valeur (return valeur)
def demande_choix_nombre(min : int, max : int) -> int:
    reponse = input(f"Choisissez un nombre entre {min} et {max}. ")
    try :
        reponse_int = int(reponse)
        if not (min <= reponse_int <= max):
            print(f"Erreur, vous devez saisir un nombre entre {min} et {max}. ")
            return demande_choix_nombre(min,max)
        print(f"Vous avez choisi {reponse_int}.") 
        return reponse_int
    except :
        print(f"Erreur, vous devez saisir un nombre entre {min} et {max}. ")
        demande_choix_nombre(min,max)

choix = demande_choix_nombre(5,10)
print(choix)

"""



"""
# démonstration différence return et break
def a():
    print("Début fonction")
    print("Début boucle")
    for i in range (20):
        if i > 10:
            print("Fin boucle")
            break
            #return
        print(i)
    print("Ceci est hors boucle.")
    print("Fin fonction")
        
a()
"""


"""
def FONCTION():
    print("toto")
    return 1

a = 5

b = FONCTION()

print("a", a, "b", b)
"""




"""
exemple des callbacks
def afficher_table_multiplication(n: int) -> None:
    for i in range(1,10):
        print(i, "x", n, "=", i*n)

def afficher_table_addition(n: int) -> None:
    for i in range(1,10):
        print(i, "+", n, "=", i+n)
    
"""





"""
#callbacks et fonction lambda
def mult_callback(a,b):
    return a*b

def add_callback(a,b):
    return a+b

def pow_callback(a,b):
    return pow(a, b)

def afficher_table(n: int,signe : str, operation_cbk) -> None: # cbk pr callback
    for i in range(1,10):
        if not (signe=="+" or signe=="-" or signe=="*" or signe=="/" or signe=="^"):
            signe = input("Veuillez saisir un signe correct +, -, * ou / ")
            return afficher_table(n,signe)
        print(i, signe, n, "=", operation_cbk(i,n))
    print()


# afficher_table(2,"*", mult_callback)
# afficher_table(2,"+", add_callback)
# afficher_table(2,"^", pow_callback)

afficher_table(2,"^", lambda a, b : pow(a,b))
"""

"""
def somme(*args):
    resultat = 0
    for n in args:
        resultat += n
    return resultat

addition = somme(1,2,3,4)
print(addition)
"""

def somme(titre : str, **args):
    resultat = 0
    for n in args.values():
        resultat += n
    return resultat

print(somme("somme des notes", maths=15, geo=11, francais=5))