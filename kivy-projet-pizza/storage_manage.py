import json

class StorageManager:
    # FONCTION POUR CHARGER LES DONNEES
    def load_data(self, data_name):
        # data_name indique sous quel nom sauver les données
        # on ait juste qu'à modifier le data_name
        try:
            filename = self.get_filename(data_name) # appel de la fonction ci-dessous
            file = open(filename, "r") # ouverture du fichier en mode lecture
            data = file.read() # les datas sont au format JSON
            file.close()
        except:
            return None # en cas d'erreur, la fonction retournera None
        return json.loads(data)  # pour désérialiser les data

    # FONCTION POUR SAUVER LES DONNEES
    def save_data(self, data_name, data_content):
        # data_name indique sous quel nom sauver les données
        # data_content indique quelles données sauvegarder
        filename = self.get_filename(data_name)  # appel de la fonction ci-dessous
        data_str = json.dumps(data_content) # sérialisation des données au format JSON pour sauvegarde
        file = open(filename, "w")  # ouverture du fichier en mode écriture
        file.write(data_str) # rédaction du fichier
        file.close()

    # FONCTION POUR SEPARER LA STRUCTURE DES FICHIERS (EXTENSIONS)
    # afin de pouvoir adapter facilement si je la modifie
    def get_filename(self, data_name):
        return data_name + ".json" # précision du format - adaptable en cas de réutilisation dans d'autres projets

