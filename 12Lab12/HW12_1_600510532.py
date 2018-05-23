#!/usr/bin/python3 # This is server.py file
import socket
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
serversocket.listen(5)


while True:
     clientsocket,addr = serversocket.accept()
     print("Got a connection from %s" %str(addr))

     while True:
          data = clientsocket.recv(1024).decode('ascii')
          if not data:
               print('$')
               break
          print('from connected user:',data)
          if data != 'q':        
               try:
                    output = str(int(data)**2)
                    print('sending:',output)
                    
               except:
                    print('cannot calculate',data)
                    output = 'cannot calculate '+data
               clientsocket.sendall(output.encode('ascii'))

     clientsocket.close()
serversocket.close()


     
     
