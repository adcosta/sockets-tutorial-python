import sys
from socket import socket, AF_INET, SOCK_DGRAM

# 1. create UDP socket
# 2. create a message and encode it because socket.sendto() takes bytes as input
# 3. send to port 6666 of host passed as parameter

PORT = 6666

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <host>")
        sys.exit(1)

    host = sys.argv[1]
    server_address = (host, PORT)

    s = socket(AF_INET, SOCK_DGRAM)
    msg = f"Hello {host}!".encode('utf-8') 
    s.sendto(msg, server_address)
    print(f"Sending message: {msg} to {host}:{PORT}")
    s.close()

if __name__ == "__main__":
    main()

