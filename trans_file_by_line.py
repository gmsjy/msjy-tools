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
    def __init__(self, addr, source_ip, file_name):
        self.addr = addr
        self.source_ip = source_ip
        self.file_name = file_name
        self.log_file = "./transinfo.log"
        self.send_sock = socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
        self.line_num = 1
        self.info = ""

    def set_logfile(self, logfile):
        ''' set the logfilename's path'''
        self.log_file = logfile
        return self

    def set_source_ip(self, source_ip):
        ''' set the source log's ip address '''
        self.source_ip = source_ip
        return self

    def loging(self):
        '''write the log to the logfile'''
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open(self.log_file, 'a+') as f:
            self.info = '\n' + current_time+' '+self.info
            f.write(self.info)

    def send(self):
        ''' send the log file for the ipaddress '''
        self.send_sock.connect(self.addr)
        try:
            with open(file_name, 'rb') as f:
                for line in f:
                    line = line.strip('\n')
                    add_source_ip = lambda log, ip: log+' '+ip
                    line_new = add_source_ip(line, self.source_ip)
                    self.send_sock.send(line_new+'\n')
                    self.line_num += 1
        except:
            self.info = "  {}  {}".format(self.file_name, self.line_num)
            self.loging()
            self.send_sock.close()
        self.info = "The {ip} logfile trans finish !"
        self.loging()
        self.send_sock.close()


if __name__ == "__main__":
    node_three = send_file(ADDR, ip, file_name)
    node_three.send()








