import json 
import socket 
import threading

ip = 'localhost'
port = 6667

def handle_client(conn, address):
	message = conn.recv(1024)
	json_response = dict(zip(['message', 'address', 'port'], [message.decode(), address[0], address[1]])) 
	conn.sendall(json.dumps(json_response).encode())
	conn.close()

def server(server_address):
	print(f"Starting server...")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	s.bind(server_address)
	s.listen(5)
	print(f"Listening for connections on {server_address}...")
	while True:
		(conn, address) = s.accept()
		print(f"Accepted new connection from {address}")
		t = threading.Thread(target=handle_client, args=(conn, address))
		t.daemon = True
		t.start()

def main():
	try: 
		server_address = (ip, port)
		server(server_address)
	except KeyboardInterrupt: 
		print(f"Keyboard interrupt")

if __name__ == '__main__':
	main()

