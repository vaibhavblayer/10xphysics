import socket

HOST = '172.20.10.3'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    conn, add = server.accept()
    print(f'Connected')
    conn.send(f'Hello there'.encode())
