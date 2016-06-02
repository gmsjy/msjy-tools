#!/bin/python
#deliver the file by the lines

from socket import *
import os
import time

ADDR = ('127.0.0.1',8888)
BUFSIZE = 1024
logfile='./transinfo.log'

ip='177.89.10.45'
filename = '/home/vagrant/web_log/http.log'
sendSock = socket(AF_INET, SOCK_STREAM)
sendSock.connect(ADDR)

def loging(logfile,info):
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(logfile, 'a+') as f:
        info = '\n' + currentTime+' '+info
        f.write(info)

def addSource(line, ip):
    return line+' '+ip

linesNum = 1

try:
    with open(filename,'rb') as f:
        for line in f:
            line = line.strip('\n')
            lineNew = addSource(line, ip)
            lineNew = lineNew + ' {} '.format(linesNum)
            sendSock.send(lineNew+'\n')
            linesNum += 1
except:
    info = "  {}  {}".format(filename, linesNum)
    loging(logfile,info)
    sendSock.close()

sendSock.close()