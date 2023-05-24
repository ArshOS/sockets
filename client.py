import socket

clt = socket.socket()

clt.connect(('server-IPv4', 9999))

print(clt.recv(1024).decode())