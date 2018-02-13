#!/usr/bin/python3
"""
Ejercicio 14.3 URLs Aleatorias

Pedro Arias Pérez
p.ariaspe @ alumnos.urjc.es
SAT , Universidad Rey Juan Carlos
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to thelocalhost
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        num = random.randrange(999999999)
        #url = 'http://localhost:1234/' + str(num)
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hola. <a href='/" +
                        bytes(str(num), 'utf-8') +
                        b"'>Dame otra<a/>" +
                        b"</body></h1></html>\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
