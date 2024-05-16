# sockets-tutorial-python

## UDP Sockets

### Very basic example of UDP server
 
  You should start the server first. It will loop forever printing all messages
  received from any client at any momment:

```bash
$ python udp-server.py
Listenning on UDP port 6667 (forever! Use Ctrl-C to stop me!)
...
```
 You need to press Ctrl-C to stop it!
 On another terminal, you may check if UDP port 6667 is in use:

```bash
$ netstat -n -a | grep 6667
udp4       0      0  127.0.0.1.6667         *.*                               
```

### Very basic example of UDP client

  The client just creates a UDP socket and sends a message:

```bash
$ python udp-client.py 
Sending message: b'Hello you there!' to localhost port 6667
```

### Client and server in same program: sending/receiving HELLO every second

```bash
$ python python udp-client-server.py 
Sending message: b'HELLO!' to 255.255.255.255 port 33333
Received message: HELLO! from ('172.25.8.195', 33333)
Sending message: b'HELLO!' to 255.255.255.255 port 33333
Received message: HELLO! from ('172.25.8.195', 33333)
...
```
  It is sending and receiving at the same time, listenning to own messages that
  are broadcasted. You can only start one instance per host.
  Press Ctrl-C to stop it.

## TCP Sockets

### Basic example of TCP server

  You should start the server firt, it will loop wait for connections on port
  6667 until Ctrl-C is pressed.

```bash
$ python tcp-server.py
Starting server...
Listening for connections on ('localhost', 6667)...
```

 On another terminal, you may check if TCP port 6667 is in use:

```bash
$ netstat -n -a | grep 6667
tcp4       0      0  127.0.0.1.6667         *.*                    LISTEN
```

### Basic example of TCP client

  To start the client excecute _python tcp-client.py_ withou parameters. It will
  connect to localhost port 6667 and ask for a message to send:
```bash
$ python tcp-client.py
Connecting to 127.0.0.1 port 6667
Enter your message: Ola Mundo!
Answer: b'{"message": "Ola Mundo!", "address": "127.0.0.1", "port": 54729}'
Closing socket
```

  Both client closes the socket after sending the messages and receiving an
  answer from the server. The server also closes de socket after sending an
  answer message to the client.

  If you start the client before the server, the program terminates with a
  socket error (connection refused):

```bash
$ python tcp-client.py
Connecting to 127.0.0.1 port 6667
Traceback (most recent call last):
  File "/Users/costa/git/sockets-tutorial-python/tcp-client.py", line 10, in
  <module>
      sock.connect(server_address)
      ConnectionRefusedError: [Errno 61] Connection refused
```


