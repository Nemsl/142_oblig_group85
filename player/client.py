import socket
import json
import pickle
import client_draw
import core

HOST = "127.0.0.1"
Local = "localhost"# The server's hostname or IP address
PORT = 65432  # The port used by the server
address = (HOST, PORT)
import socket
Champion = 'Test'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Local, PORT))
    s.sendall(b"Connected")
    printer2 = s.recv(4096)
    d = pickle.loads(printer2)
    while True:
        print(client_draw.print_available_champs(d))
        Message = s.recv(2048)
        try:
            Message = Message.decode()
        except:
            client_draw.print_match_summary(pickle.loads(Message))
        try:
            if "Velg" in Message:
                inp = input(">")
                if inp == "q":
                    break
                s.sendall(inp.encode())
            else:
                continue
        except:
            break



