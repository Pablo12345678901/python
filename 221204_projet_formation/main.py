# album
# artistes -> MJ, CD
# albums -> Thriller, ABC, DEF
# artist ID 1 / 2 -> manuellement puis avec le counter

import sqlite3
# import du module sqlite3
connexion = sqlite3.connect("album2.db")
# établir une connection avec le fichier sql (créer s'il n'exite pas)
curseur = connexion.cursor()
# création du curseur
curseur.execute(""" CREATE TABLE artiste(
                    artiste_id INTEGER NOT NULL PRIMARY KEY,
                    nom VARCHAR
                    );""")
# exécution des instructions 1 par 1
curseur.execute("""CREATE TABLE album(
                    album_id INTEGER NOT NULL PRIMARY KEY,
                    artiste_id INTEGER REFERENCES artiste,
                    titre VARCHAR,
                    annee_sortie INTEGER
                    );""")
curseur.execute('INSERT INTO artiste (nom) VALUES ("Michael Jackson");')
mj_id = curseur.lastrowid
curseur.execute('INSERT INTO artiste (nom) VALUES ("Céline Dion");')
cd_id = curseur.lastrowid
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(mj_id) + ', "Thriller", 2022);')
# usage des guillemets simples pour appeler la variable mj_id sinon elle est considérée comme du texte
# besoin du str car pas possible de concaténer des int avec des str
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(cd_id) + ', "l\'abc", 222);')
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(cd_id) + ', "def", 333);')
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(mj_id) + ', "zzz", 4044);')

connexion.commit()
# commit pour s'assurer que tout est bien écrit dans la base de données
connexion.close()
# clôturer le fichier une fois terminé
# une fois fait, faire glisser le fichier sur l'application ouvert sqlite pour voir le rendu

