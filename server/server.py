# echo-server.py

import socket
import selectors
import types
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


#AF_INET - use ipv4 addresses
#SOCK_STREAM - use tcp
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(b"Messege sendt")
