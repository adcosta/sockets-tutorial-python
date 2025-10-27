from socket import socket, AF_INET, SOCK_DGRAM 

# 1. create UDP socket 
# 2. listen on port 6666 with 8KB buffer
# 3. loop forever receiving and printing message

PORT = 6666

def main():
    listen_address = ("", PORT)
    sock = socket(AF_INET, SOCK_DGRAM)
    try:
        sock.bind(listen_address)

        print(f"Listening on UDP port {PORT} forever! Ctrl-C to stop...")
        while True:
            msg, addr = sock.recvfrom(8192)
            text = msg.decode("utf-8", errors="ignore")
            print(f" --> message from {addr}: {text}")
    except KeyboardInterrupt:
         print("\nStopping...")
    finally:
         sock.close()

if __name__ == "__main__":
    main()

