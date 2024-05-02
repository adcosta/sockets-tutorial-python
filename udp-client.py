from socket import socket, AF_INET, SOCK_DGRAM

# create UDP socket
# send to localhost port 6667
# socket.sendto() takes bytes as input, hence we must encode the string first.
# send to localhost port 6667

s = socket(AF_INET, SOCK_DGRAM)
msg = ("Hello you there!").encode('utf-8') 
s.sendto(msg, ('localhost', 6667))
print(f"Sending message: {msg} to localhost port 6667")


