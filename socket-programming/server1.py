# server
import socket, threading

bind_ip = "0.0.0.0" 
bind_port = 9999 

# socket object
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print("[*] Server open. Listening to %s:%d" %(bind_ip, bind_port))

# function to handle every client connection
def handle_client(client_socket):
    # receive and print data from client
    message = client_socket.recv(1024).decode()
    print("[*] Received: %s" %(message))

    message2 = "server got your data."
    client_socket.send(message2.encode())
    client_socket.close()

while True:
    client,addr = server.accept()
    print("[*] Accepted connection from %s:%i" %(addr[0],addr[1]))

    # create thread every time client makes connection
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
