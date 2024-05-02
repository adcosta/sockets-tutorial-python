from socket import socket, AF_INET, SOCK_DGRAM 

# create UDP socket 
# listen on localhost port 6667 with 8KB buffer
# loop forever receiving and printing message
sock = socket(AF_INET, SOCK_DGRAM) 
sock.bind(('localhost', 6667))
print("Listenning on UDP port 6667 (forever! Use Ctrl-C to stop me!)")
while True:
	msg, addr = sock.recvfrom(8192) 
	print("Got message from %s: %s" % (addr, msg.decode()))
