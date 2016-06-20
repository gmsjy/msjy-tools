#!/bin/python
# deliver the file by the lines


from socket import *
import os
import time
from multiprocessing import Pool

ADDR = ('127.0.0.1', 8888)
BUFSIZE = 1024
logfile = './transinfo.log'

ip='177.89.10.45'
file_name = '/home/vagrant/web_log/http.log'



class send_file(object):
    ''' class for the file send '''
    def __init__(self, addr , source_ip, file_name, send_sock):
        self.addr = addr
        self.log_file = "./transinfo.log"
        self.send_sock = send_sock
        self.line_num = 1

    def set_logfile(self, logfile):
        self.log_file = logfile
        return self

    def loging(self, info):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open(self.log_file, 'a+') as f:
            info = '\n' + currentTime+' '+info
            f.write(info)

    def send(self, log_file_name, source_ip):
        self.send_sock.connect(self.addr)
        try:
            with open(file_name,'rb') as f:
                for line in f:
                    line = line.strip('\n')
                    add_source_ip = lambda log,ip: log+' '+ip
                    line_new = add_source_ip(line, source_ip)
                    # lineNew = lineNew + ' {} '.format(linesNum)
                    sendSock.send(line_new+'\n')
                    self.line_num += 1
        except:
            info = "  {}  {}".format(log_file_name, self.line_num)
            self.loging(info)
            self.send_sock.close()
        info = "The {ip} logfile trans finish !"
        self.loging(info)
        self.send_sock.close()


if __name__ == "__main__":
    send_sock = socket(AF_INET, SOCK_STREAM)
    node3 = send_file(ADDR,logfile,send_sock)
    node3.send(file_name,ip)








