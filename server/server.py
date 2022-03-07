# echo-server.py

import socket
import selectors
from selectors import EVENT_READ
import types
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

sel = selectors.DefaultSelector()
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print(f"Listening on {(HOST, PORT)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)
#AF_INET - use ipv4 addresses
#SOCK_STREAM - use tcp

def accept(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    sel.register(conn, EVENT_READ)

def read(conn):

    recv_data = conn.recv(2048)  # Should be ready to read
    if recv_data:
        print(recv_data.decode())
    else:
        print(f"Closing connection to {recv_data.addr}")
        sel.unregister(recv_data)
        recv_data.close()



try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept(key.fileobj)
            else:
                read(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()