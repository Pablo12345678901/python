from sockets_serveur import envoi_message, reception_message, MAX_SIZE
import socket
import time
HOST_IP = "127.0.0.1"
HOST_PORT = 32000


temps_avant_nouvelle_tentative = 1
while True: 
    try:
        s = socket.socket()  
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR : impossible de se connecter au serveur")
        print(f"Nouvelle tentative dans {temps_avant_nouvelle_tentative} secondes")
        time.sleep(temps_avant_nouvelle_tentative)
    else:
        print("Connecté au serveur.")
        break

while True:
    data_recues = s.recv(MAX_SIZE)
    print("Message : ", data_recues.decode())
    message = input("Vous : ")
    s.sendall(message.encode())
    
s.close()
print(f"Connexion au serveur IP : {HOST_IP}, Port {HOST_PORT}.")

