import socket

clt = socket.socket()

clt.connect(('192.168.31.124',12304))

n = input ("Enter a name ")
clt.send(bytes(n,'utf-8'))

print(clt.recv(1024).decode())