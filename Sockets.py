import socket

server = socket.socket()
print("Socket created")
server.bind(('192.168.31.124',12304))

server.listen(8)
print("Waiting for connection..")

while True:
    client, addr = server.accept()
    N = client.recv(1024).decode()
    print("Connected with  ", addr, N)
    
    client.send(bytes("Welcome to the Demo Server",'utf-8'))
    
    client.close() 

      