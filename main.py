import socket
import log
import requesthandler
import time
#import sys
#import thread
#import args

sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('127.0.0.1',80))

sock.listen(5)

print ("python server started.....")

while True:
    connection, address = sock.accept()
    
    request = connection.recv(4096)

    response = requesthandler.requesthandler(str(request))

    connection.send(response)

    log.log(address,str(time.ctime()),request)

    connection.close()
    
sock.close()
