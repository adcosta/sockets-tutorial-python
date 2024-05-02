from socket import socket, AF_INET, SOCK_STREAM

ip = '127.0.0.1'
port = 6667
server_address = (ip, port)

# Create a TCP/IP socket and connect to server
print(f"Connecting to {ip} port {port}")
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(server_address)

# send messages to server
message = input("Enter your message: ")
sock.send(message.encode())

# receive answer
answer = sock.recv(1024)
print(f"Answer: {answer}")

# close the socket
print("Closing socket")
sock.close()

