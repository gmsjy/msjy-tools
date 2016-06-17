#!/bin/python
# deliver the file by the lines


import socket
import os
import time
from multiprocessing import Pool

ADDR = ('127.0.0.1', 8888)
BUFSIZE = 1024
logfile = './transinfo.log'

ip='177.89.10.45'
filename = '/home/vagrant/web_log/http.log'



class send_file(object):
    ''' class for the file send '''
    def __init__(self, addr, log_file):
        self.addr = addr
        self.log_file = log_file
        self.send_sock = socket.socket(AF_INET, SOCK_STREAM)
        self.line_num = 1

    def loging(self, info):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open(self.log_file, 'a+') as f:
            info = '\n' + currentTime+' '+info
            f.write(info)

    def send(self, log_filename, source_ip, log_file):
        self.send_sock.connect(self.addr)
        try:
            with open(filename,'rb') as f:
                for line in f:
                    line = line.strip('\n')
                    add_source_ip = lambda log,ip: log+' '+ip
                    line_new = addSource(line, source_ip)
                    # lineNew = lineNew + ' {} '.format(linesNum)
                    sendSock.send(line_new+'\n')
                    self.line_num += 1
        except:
            info = "  {}  {}".format(log_filename, self.line_num)
            self.loging(info)
            self.send_sock.close()
        info = "The {ip} logfile trans finish !"
        self.loging(info)
        self.send_sock.close()


if __name__ == "__main__":
    node3 = send_file(ADDR,logfile)
    node3.send(filename,ip)








