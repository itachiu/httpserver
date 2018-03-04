import scoket
import thread
import time
import request_hadler
import log_files

cofigurations = open('settings.conf','r')
list_of_config = []

for i in configurations.readlines():
    list_of_config.append(i)
    list_of_config[
    
socket_listining = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_listining.bind((ip_adresses,port))

socket_listining.listen(5)

connection,client_address = socket_listining.accept()

request_recived = connection.recv(4096)

request_handler.request_handler(request_recived)

log_files.log(client_address,time.ctime())






