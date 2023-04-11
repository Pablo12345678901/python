#CREATION DE FICHIER ZIP
import shutil
shutil.make_archive("fichier_excel234", "zip", "/Users/alejandramt/Desktop/Développement/221211")
# besoin de préciser en paramètre :
#   le nom du fichier
#   son extension (zip) car cette fonction permet aussi de produire un fichier en extension "tar"
#   le répertoire à zipper (path relatif ou complet)

#import zipfile
#import shutil

#shutil.unpack_archive("fichier")