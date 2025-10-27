# sockets-tutorial-python

## UDP Sockets

### Very basic example of UDP server
 
  You should start the server first. It will loop forever printing all messages
  received from any client at any momment:

```bash
$ python udp-server.py
Listening on UDP port 6666 forever! Ctrl-C to stop...
...
```
 You need to press Ctrl-C to stop it!
 On another terminal, you may check if UDP port 6666 is in use:

```bash
$ netstat -n -a | grep 6666
udp4       0      0  127.0.0.1.6666         *.*                               
```

### Very basic example of UDP client

  The client just creates a UDP socket and sends a message:

```bash
$ python udp-client.py 127.0.0.1
Sending message: b'Hello 127.0.0.1!' to 127.0.0.1:6666
...
```

### Client and server in same program: sending/receiving HELLO every second

```bash
$ python python udp-client-server.py 
--> Sending message: b'HELLO!' to 255.255.255.255 port 33333
<-- Received message: HELLO! from ('192.168.1.44', 33333)
--> Sending message: b'HELLO!' to 255.255.255.255 port 33333
<-- Received message: HELLO! from ('192.168.1.44', 33333)
--> Sending message: b'HELLO!' to 255.255.255.255 port 33333
<-- Received message: HELLO! from ('192.168.1.44', 33333)
--> Sending message: b'HELLO!' to 255.255.255.255 port 33333
<-- Received message: HELLO! from ('192.168.1.44', 33333)

...
```
  It is sending and receiving at the same time, listenning to own messages that
  are broadcasted. You can only start one instance per host.
  Press Ctrl-C to stop it.

## TCP Sockets

### Basic example of TCP server

  You should start the server firt, it will loop wait for connections on port
  6666 until Ctrl-C is pressed.

```bash
$ python tcp-server.py
Starting server...
Listening for connections on ('', 6666)...
```

 On another terminal, you may check if TCP port 6666 is in use:

```bash
$ netstat -n -a | grep 6666
tcp4       0      0  127.0.0.1.6666         *.*                    LISTEN
```

### Basic example of TCP client

  To start the client excecute _python tcp-client.py_ with 'server' as argument. It will
  connect to that server on port 6666 and ask for a message to send:
```bash
$ python tcp-client.py 127.0.0.1
Connecting to localhost port 6666
Enter your message: Hello!
Answer: b'{"message": "Hello!", "address": "127.0.0.1", "port": 61135}'
Closing socket
```

  Client closes the socket after sending the messages and receiving an
  answer from the server. The server also closes de socket after sending an
  answer message to the client.

  If you start the client before the server, the program terminates with a
  socket error (connection refused):

```bash
$ python tcp-client.py localhost
onnecting to localhost port 6666
Traceback (most recent call last):
  File "/Users/costa/git/sockets-tutorial-python/tcp-client.py", line 36, in <module>
    main()
    ~~~~^^
  File "/Users/costa/git/sockets-tutorial-python/tcp-client.py", line 21, in main
    sock.connect(server_address)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^
ConnectionRefusedError: [Errno 61] Connection refused

```


