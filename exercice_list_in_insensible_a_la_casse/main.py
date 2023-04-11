# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"

def a_extension(nom_du_fichier : str) -> bool:
    #indique s'il y a une extension.
    return (nom_du_fichier.find(".") != -1)


def extraction_extension(nom_du_fichier: str) -> str:
    splitage = nom_du_fichier.split(".")
    return splitage[-1]


def correspondance_extensions(nom_du_fichier : str,dict_definition_extension : list) -> str:
    if a_extension(nom_du_fichier):
        extension = extraction_extension(nom_du_fichier).lower()
        if extension in dict_definition_extension:
            return dict_definition_extension[extension]
        else:
            return "Extension non connue"
    else:
        return "Aucune extension"


def affichage_extension(nom_du_fichier : str,dict_definition_extension : list) -> None:
    print(nom_du_fichier, "(" + correspondance_extensions(nom_du_fichier,dict_definition_extension) + ")")
    nouvel_element = nom_du_fichier + " (" + correspondance_extensions(nom_du_fichier,dict_definition_extension) + ")"
    return nouvel_element

fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

dict_definition_extension = {
                                "doc" : "Document Word",
                                "txt" : "Document Texte",
                                "jpeg" : "Image JPEG",
                                "exe" : "Executable",
}


liste_1 = [affichage_extension(nom_du_fichier,dict_definition_extension) for nom_du_fichier in fichiers]
print()
liste_2 = []
for fichier in fichiers:
    if len(fichier.split(".")) > 1:
        extension_eee = fichier.split(".")[-1]
        if extension_eee.lower() in dict_definition_extension:
            extension_eee = dict_definition_extension[extension_eee.lower()]
        else:
            extension_eee = "Extension non connue"
    else:
        extension_eee = "Aucune extension"
    nouvel_element = fichier + " (" +extension_eee + ")"
    liste_2.append(nouvel_element)
print(liste_1)
print(liste_2)
"""
for fichier in fichiers:
    print(fichier, correspondance_extensions(nom_du_fichier,dict_definition_extension))
"""


'''
RESULTAT ATTENDU
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte) > recherche insensible à la caisse
vacances.jpeg (Image JPEG)
planning (Aucune extension) > annonce si pas d'extension
data.dat (Extension non connue) > annonce si extension inconnue
'''

# lower/upper
# in / index / for
# split
# -1

# extraire extension

# faire la correspondance définition