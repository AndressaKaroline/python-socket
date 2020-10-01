import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = sock.bind(('localhost', 9000))
sock.listen(1)

msg = "Bem vindo ao chat"
msg_size = len(msg)

print("Aguardando conexao")
connection, address_client = sock.accept()    

connection.sendall(str(msg_size).zfill(4).encode())
connection.sendall(msg.encode())

while True:
    expected_data_size = ''  
    while(expected_data_size == ''):
        expected_data_size += connection.recv(4).decode()
    expected_data_size = int(expected_data_size)
    
    received_data = ''
    while len(received_data) < expected_data_size:
        received_data += connection.recv(4).decode()
    print("Cliente: " + received_data)

    if received_data.lower() == "see ya":
        print("Chat finalizado!")
        break

    msg = raw_input("Mensagem: ").strip()
    send_data_size = len(msg)
    connection.sendall(str(send_data_size).zfill(4).encode())
    connection.sendall(msg.encode())
        
    if msg.lower() == "see ya":
        print("Chat finalizado!")
        break

connection.close()
