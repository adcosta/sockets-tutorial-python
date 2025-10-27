import sys
from socket import socket, AF_INET, SOCK_STREAM

# 1. create TCP socket
# 2. create a message and encode 
# 3. send to port 6666 of host passed as parameter

PORT = 6666

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <host>")
        sys.exit(1)

    host = sys.argv[1]
    server_address = (host, PORT)

    # Create a TCP/IP socket and connect to server
    print(f"Connecting to {host} port {PORT}")
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

if __name__ == "__main__":
    main()

