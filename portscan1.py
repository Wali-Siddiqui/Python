#!/usr/bin/python3
import socket
from termcolor import colored
# for TCP packets 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2 Seconds set for default timeout
socket.setdefaulttimeout(2)

host = input("[*] Enter the Host to Scan: ")

def port_scanner(port):
    if sock.connect_ex((host,port)):
        print (colored("[!!] Port %s is closed" % port,'red'))    
    else:
        print (colored ("[+] Port %s is open" % port,'green'))

for port in range(1,1000):
    port_scanner(port)

