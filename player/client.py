import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
address = (HOST, PORT)
from socket import socket


sock = socket()
sock.connect(address)
message = "Hei"
sock.send(message.encode())
