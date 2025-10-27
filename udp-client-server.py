import socket
import time
from threading import Thread

# define destination address and port
destination_address = '255.255.255.255'
PORT = 33333

# create a time triggered event to send "HELLO" every second
def send_message(sock, msg): 
    while True:
        print(f"--> Sending message: {msg} to {destination_address} port {PORT}")
        sock.sendto(msg, (destination_address, PORT))
        time.sleep(1)  

def receive_message(sock):
    while True:
        message, address = sock.recvfrom(1024)
        print(f"<-- Received message: {message.decode()} from {address}")

def main():
    # create a UDP socket and set it to broadcast and address reusing
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind the socket to port on all local IP addresses
    sock.bind(('', PORT))

    # prepare hello message
    message = ("HELLO!").encode('utf-8')

    # start the sending and receiving threads
    receive_thread = Thread(target=receive_message, args=(sock,), daemon=True)
    receive_thread.start()
    send_thread = Thread(target=send_message, args=(sock, message), daemon=True)
    send_thread.start()

    # main thread waits for others to finish
    send_thread.join()
    receive_thread.join()

if __name__ == "__main__":
    main()

