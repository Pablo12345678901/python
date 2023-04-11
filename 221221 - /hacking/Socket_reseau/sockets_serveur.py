import socket

def envoi_message(socket):
    message = input("Vous : ")
    #print("Vous :"+message)
    message_en_bites = message.encode()
    socket.sendall(message_en_bites)

def reception_message(socket, MAX_SIZE):
    message_recu = socket.recv(MAX_SIZE)
    message_recu_decode = message_recu.decode()
    if message_recu:
        print("Message : "+message_recu_decode)
    else:
        reception_message(socket, MAX_SIZE)


HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_SIZE = 1024

if __name__ == '__main__':
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST_IP, HOST_PORT))
    s.listen()
    print(f"Attente de connexion sur IP : {HOST_IP} / Port : {HOST_PORT}")
    connection_socket, client_address = s.accept()
    print(f"Connexion établie avec {client_address}")
    
    while True:
        message = input("Vous : ")
        connection_socket.sendall(message.encode())
        data_recues = connection_socket.recv(MAX_SIZE)
        print("Message : ", data_recues.decode())

    s.close()
    connection_socket.close()
