import socket
import time
from threading import Thread

# define destination address
destination_address = '255.255.255.255'
# define server port
port = 33333

# create a UDP socket and set it  to broadcast and address reusing
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to port on all local IP addresses
sock.bind(('', port))

# create a time triggered event to send "HELLO" every second
def send_message(msg): 
	while True:
		print(f"Sending message: {msg} to {destination_address} port {port}")
		sock.sendto(msg, (destination_address, port))
		time.sleep(1)  

def receive_message():
	while True:
		message, address = sock.recvfrom(1024)
		print(f"Received message: {message.decode()} from {address}")

# start the sending and receiving threads
message = ("HELLO!").encode('utf-8')
send_thread = Thread(target=send_message, args=(message,))
receive_thread = Thread(target=receive_message)
receive_thread.start()
send_thread.start()

# main thread waits for others to finish
send_thread.join()
receive_thread.join()
