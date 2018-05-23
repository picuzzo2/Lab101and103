#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


host = socket.gethostname()                           
port = 9999
s.connect((host, port))                               

sendMSG = input().encode('utf-8')
#sendMSG = sendMSG
s.sendall(sendMSG)

while 1:
    # Receive no more than 1024 bytes
    msg = s.recv(1024)
    msg = msg.decode('ascii')
    print('Receive from server:',msg)

    output = input()
    if output != 'q':
        s.sendall(output.encode('utf-8'))
    else:
        print('$')
        break
s.close()