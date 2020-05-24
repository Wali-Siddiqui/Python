import socket
import sys

# Parameters
tcp_ip = '127.0.0.1'
tcp_port = 8090
buffer_size = 1024
message = "Im sending data"


try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # SOCK_STREAM for TCP
                                                                      # AF_INET for IPV4   
except socket.error as e:                                                  
    print("Error occured while creating socket:", + str(e[0])+', Error message :' + e[1])
    sys.exit

tcp_socket.connect((tcp_ip,tcp_port))

try:
    tcp_socket.send(message.encode())
except socket.error as e: 
    print("Error occured while creating socket:", + str(e[0])+', Error message :' + e[1])
    sys.exit()
print('Message to the server send sucessfully')

data = tcp_socket.recv(buffer_size)
print(data)
tcp_socket.close()


