import socket
import sys
from _thread import *

TCP_IP = '127.0.0.1'
TCP_PORT = 8090

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Error occured while creating socket:", + str(e[0])+', Error message :' + e[1])
    sys.exit

#Bind socket to host and port

tcp_socket.bind((TCP_IP,TCP_PORT))
tcp_socket.listen(10)
print("Im listening")

def client_connections_handler(connection):
    Buffer_size = 1024
    while True:
        data = connection.recv(Buffer_size)
        print(data)
        reply = 'Data Received:' + str(data)
        if not data:
            break
        connection.sendall(reply.encode())
    connection.close()
while True:
    connection,address = tcp_socket.accept()
    print ("Client connected" , address)
    start_new_thread(client_connections_handler,(connection,))
tcp_socket.close()