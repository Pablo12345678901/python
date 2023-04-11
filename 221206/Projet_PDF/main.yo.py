"""
contenu_de_sortie = PdfFileWriter()
fichier_pdf_presentation = open("presentation.pdf", "rb")
# l'extension par défaut est texte > besoin d'ouvrir en binaire avec "rb"
fichier_pdf_recap = open("recap.pdf", "rb")
reader_presentation = PdfFileReader(fichier_pdf_presentation)
# reader permet d'extraire les information du pdf
reader_recap = PdfFileReader(fichier_pdf_recap)
print("Nombre de pages du fichier recap.pdf : " + str(reader_recap.getNumPages()))
# getNumPages indique le nombre de page sous forme d'un int
contenu_de_sortie.addPage(reader_presentation.getPage(0).rotateClockwise(90*4*100))
# addPage ajoute une page au fichier "contenu_de_sortie"
# getPage récupére la page à l'index 0 = page 1 du fichier "recap"
for i in range (reader_recap.getNumPages()):
    contenu_de_sortie.addPage(reader_recap.getPage(i))
# boucler pour ajouter toutes les autres pages provenant du fichier "presentation"
fichier_sortie = open("fichier_sortie123.pdf", "wb")
# on rédige le fichier de sortie en binaire
contenu_de_sortie.write(fichier_sortie)
# avec write, j'écris du contenu dans le fichier de sortie
fichier_sortie.close()
fichier_pdf_presentation.close()
# ne pas fermer les fichiers avant d'avoir rédigé le nouveau fichier, sinon rédaction avec page blanche
fichier_pdf_recap.close()
"""
from PyPDF2 import PdfFileWriter, PdfFileReader

f = open("recap.pdf", "rb")
# ouvrir le fichier "recap.pdf" en mode lecture (binaire, pas texte)
reader_recap = PdfFileReader(f)
# lire le fichier et le stocker dans une variable
page0 = reader_recap.getPage(1)
# récupérer la première page à l'index 0 et la placer dans une variable
texte_recupere = page0.extractText()
# extraire le texte de la première page
# CORRECTION DES CARACTERES SPECIAUX AVEC REPLACE
texte_recupere = texte_recupere.replace("Ò", '"')
texte_recupere = texte_recupere.replace("‘","è")
texte_recupere = texte_recupere.replace("”","é")
texte_recupere = texte_recupere.replace("!"," ")
texte_recupere = texte_recupere.replace("Õ","'")
texte_recupere = texte_recupere.replace("‹","à")
texte_recupere = texte_recupere.replace("È","»")
texte_recupere = texte_recupere.replace("’","ê")
# possible enchaîner en faisant ...replace(...).replace(...).replace(...)

print(texte_recupere)
# l'afficher / le print pourrait aussi être après le close
f.close()

# L'encodage des caractères spéciaux dépendent du programme qui a créé le PDF.
# Pour y remédier, besoin d'utiliser la fonction replace caractère spécial par caractère spécial.
# le header est extrait à la fin du texte produit (à cause de la hiérarchie du PDF).
# les caractères non supportés sont :
# " (guillemets doubles)> remplacé par Ò
# è remplacé par ‘
# é remplacé par ”
# “ remplacé par Ò
# ESPACE"remplacé par !Ò
# ' remplacé par Õ
# les tabulations
