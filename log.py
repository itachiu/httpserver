import time

def log(address, time, request ):

    log_file= open('logs.txt','a')

    log_request = open('requestlog.txt','a')

    log_to_write = str(address)+'\t'+str(time)+'\n'

    log_request_write = str(time)+'\n'+str(request)+'\n'

    log_request.write(log_request_write)

    log_file.write(log_to_write)

    log_file.close()

    log_request.close()
