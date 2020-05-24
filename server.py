import socket
import sys
# Parameters
tcp_ip = '127.0.0.1'
tcp_port = 8090
buffer_size = 1024

try:
     tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # SOCK_STREAM for TCP  
                                                                       # AF_INET for IPV4  
except socket.error as e:
       print("Error occured while creating socket:", + str(e[0])+', Error message :' + e[1])
       sys.exit()

tcp_socket.bind((tcp_ip,tcp_port))
tcp_socket.listen(2)
connection,address = tcp_socket.accept()                 
data = connection.recv(buffer_size)
print('connected with',address)
print ("Message from the client: ",data)
msg = 'Thank you for connecting us'
connection.sendall(msg.encode())
connection.close()
