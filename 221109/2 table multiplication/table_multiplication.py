# Tables de multiplication de 1 à 10x
# message d'erreur si min > max -> provoque sortie fonction (return)

"""
afficher_table_muplication
    -> contrôler que min <= max
    -> calculer les valeurs de résultats de la table
    -> afficher les calculs et résultats de la table
"""

"""
def afficher_table_muplication(numero_table: int, min: int = 1 , max: int = 10 ) -> None:
    if controle_min_plus_pt_que_max(min,max):
        calcul_multiplication_et_affichage(numero_table,min,max)

def controle_min_plus_pt_que_max(min: int,max: int):
    if not (min <= max):
        print("Erreur : Vous ne pouvez pas saisir un minimum supérieur au maximum.")
        return False
    return True

def calcul_multiplication_et_affichage(numero_table:int,min:int, max:int, ):
    for i in range(min,max+1):
        print(i, "*", numero_table, "=", i*numero_table)


afficher_table_muplication(numero_table = 5,min = 1,max = 10)
"""


def afficher_table_muplication(numero_table: int, min: int = 1 , max: int = 10 ) -> None:
    if not (min <= max):
        print("\nErreur : Vous ne pouvez pas saisir un minimum supérieur au maximum.\n")
        return None
    print()
    for i in range(min,max+1):
        print(i, "*", numero_table, "=", i*numero_table)
    print()


afficher_table_muplication(numero_table = 5,min = 1,max = 10)