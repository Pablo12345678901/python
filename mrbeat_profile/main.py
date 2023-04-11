# IMPORT SYSTEMATIQUE
import timeit
# IMPORT LIE AU CODE EN COURS DE TEST
from array import array


# VARIABLES DU CODE A TESTER
nb_samples = 44100
buf = array('h', b"\x00\x00" * nb_samples)
buf1 = array('h', b"\x00\x00" * nb_samples)  # adaptation de la taille du buffer via une allocation de mémoire avec taille maximale
buf2 = array('h', b"\x00\x00" * nb_samples)
buf3 = array('h', b"\x00\x00" * nb_samples)
buf4 = array('h', b"\x00\x00" * nb_samples)
bufs = [buf1, buf2, buf3, buf4]



# FONCTION A COMPARER
def func1():
    for i in range(0, nb_samples):
        buf[i] = 0
    return buf

def func2():
    return buf[0:nb_samples]

def func3():
    for i in range(0, nb_samples):  # pour chaque step de tous les tracks
        buf[i] = 0  # mis à 0 de la i ème valeur du buf
        for j in range(0, len(bufs)):  # pour tous les buffer
            buf[i] += bufs[j][i]  # récupération du i ème élément et addition car chaque son est une onde qui s'additionne
    return buf

def func4():
    sum_of_lists = [sum(x) for x in zip(*bufs)]
    return array('h', sum_of_lists)

def func5():
    sum_of_lists = map(sum, zip(*bufs))
    return array('h', sum_of_lists)



# CALCUL DES TEMPS POUR CHAQUE FONCTION
############################################################
# DONNEES A ADAPTER
str_name_of_functions_to_compare = ["func4", "func5"] # Mettre les noms des fonctions sous format string
repetition = 3 # Nb de répétitions
nb_tests = 1000 # Nb de test par répétition
# FIN DES DONNEES A ADAPTER
############################################################
# NE PAS MODIFIER CI-DESSOUS
part_of_setup = "from __main__ import "
str_setup = [part_of_setup+str(str_name_of_functions_to_compare[0]),part_of_setup+str(str_name_of_functions_to_compare[1])]
# CALCUL DU TEMPS D'EXECUTION MINIMAL OBTENU
time_list_for_func1 = timeit.repeat(setup=str_setup[0], stmt=str_name_of_functions_to_compare[0], repeat=repetition, number=nb_tests)
time_list_for_func2 = timeit.repeat(setup=str_setup[1], stmt=str_name_of_functions_to_compare[1], repeat=repetition, number=nb_tests)
# CALCUL DES DELTAS TEMPS ENTRE LES 2 FONCTIONS
delta_between_1_and_2 = []
for i in range(0, len(time_list_for_func1)):
    delta_between_1_and_2.append(time_list_for_func2[i]-time_list_for_func1[i])
# AFFICHAGE DES DELTAS ET RAPPORTS ENTRE LES FONCTIONS
for i in range(0, len(delta_between_1_and_2)):
    print("delta de "+ str(delta_between_1_and_2[i]) + " secondes")
    rapport = time_list_for_func1[i]/time_list_for_func2[i]
    print("La fonction "+ str_name_of_functions_to_compare[0] + " prend " + str(time_list_for_func1[i]) + " secondes.")
    print("La fonction "+ str_name_of_functions_to_compare[1] + " prend " + str(time_list_for_func2[i]) + " secondes.")
    print("La fonction "+ str_name_of_functions_to_compare[1] + " prend "+ str(rapport) +" fois moins de temps que la fonction "+ str_name_of_functions_to_compare[0] +".")
    print() # espace esthétique