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

def print_available_champs(champions: dict[heroes]) -> None:

    # Create a table containing available champions
    available_champs = Table(title='Available champions')

    # Add the columns Name, probability of rock, probability of paper and
    # probability of scissors
    available_champs.add_column("Name", style="cyan", no_wrap=True)
    available_champs.add_column("prob(:raised_fist-emoji:)", justify="center")
    available_champs.add_column("prob(:raised_hand-emoji:)", justify="center")
    available_champs.add_column("prob(:victory_hand-emoji:)", justify="center")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Local, PORT))
    s.sendall(b"Hello, world")
    while True:
        data = s.recv(2048).decode()
        heroes = json.loads(data.decode())
        print('Received from server: ' + data)

        inp = input(">")
        s.sendall(inp.encode())


'''
sock = socket()
sock.connect(address)
message = "Hei"
sock.send(message.encode())
'''