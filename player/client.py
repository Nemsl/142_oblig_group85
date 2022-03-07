import socket

HOST = "127.0.0.1"
Local = "localhost"# The server's hostname or IP address
PORT = 65432  # The port used by the server
address = (HOST, PORT)
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Local, PORT))
    s.sendall(b"Hello, world")
    while True:
        inp = input(">")
        s.sendall(inp.encode())
    data = s.recv(2048)
'''
sock = socket()
sock.connect(address)
message = "Hei"
sock.send(message.encode())
'''