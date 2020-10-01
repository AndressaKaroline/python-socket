import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9000))

while True:
    expected_data_size = int(sock.recv(4).decode())
    received_data = ''
    
    while len(received_data) < expected_data_size:
        received_data += sock.recv(4).decode()
    print("Servidor: " + received_data)

    if received_data.lower() == "see ya":
        print("Chat finalizado!")
        break
        
    msg = raw_input("Mensagem: ").strip()
    send_data_size = len(msg)
    sock.sendall(str(send_data_size).zfill(4).encode())
    sock.sendall(msg.encode())
    
    if msg.lower() == "see ya":
        print("Chat finalizado!")
        break
    
sock.close()