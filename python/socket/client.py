import socket

HOST = '172.20.10.3'
PORT = 9090

client = socket.socket()
client.connect((HOST, PORT))

print(client.recv(1024).decode())
