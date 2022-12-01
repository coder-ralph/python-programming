# client
import socket

target_host = input("enter server ip address:") # input the ip address of your machine
# target_host = "127.0.0.1"
# target_host = "192.168.1.217"
target_port = 9999

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))

print("[*] Connection to server ok")
message = input("enter your message:")
client.send(message.encode())

response = client.recv(1024).decode()
print(response)
