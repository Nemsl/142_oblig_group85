# echo-server.py
import json
import socket
import selectors
from selectors import EVENT_READ
import startGame
import champlistloader
import pickle
import core

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

players = []


DATABASE_PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, DATABASE_PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        data = conn.recv(1024 * 4)
        heroes = json.loads(data.decode())

    conn.close()
    s.close()

sel = selectors.DefaultSelector()
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print(f"Listening on {(HOST, PORT)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, True)
#AF_INET - use ipv4 addresses
#SOCK_STREAM - use tcp


def accept(sock):
    print("DEN KJØRER")
    print(sock)

    conn, addr = sock.accept()  # Should be ready to read
    conn.send(''.encode())
    print(f"Accepted connection from {addr}")
    conn.setblocking(1)
    players.append([conn, addr])
    sel.register(conn, EVENT_READ)


def read(conn):
    recv_data = conn.recv(2048)  # Should be ready to read
    if recv_data:
        print(recv_data.decode())
        #sel.register(conn, EVENT_READ)
        return recv_data.decode()


    else:
        #print(f"Closing connection to {recv_data.addr}")
        print("Closing connection")
        sel.unregister(recv_data)
        recv_data.close()





x = True
try:
    while x:
        print(x)
        events = sel.select(timeout=None)
        for key, mask in events:

            if key.data:
                accept(key.fileobj)
            else:
                read(key.fileobj)
        if len(players) == 2:
            print(players)
            x = False
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")


print("hei")



def main(chumps) -> None:

    print('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')

    champions = champlistloader.load_some_champs(chumps)
    startGame.print_available_champs(champions)
    print('\n')
    melding1 = pickle.dumps(champions)
    players[0][0].send(melding1)
    players[1][0].send(melding1)

    player1 = []
    player2 = []
    counter = 0
    # Champion selection
    while counter < 5:
        if counter % 2 == 0:
            players[0][0].send(b"Velg en sjampinjong")
            if startGame.input_champion('Player 1', 'red', champions, player1, player2, read(players[0][0])):
                counter += 1
            else:
                print("Player 1 funket ikkeqq")
                counter = 0
        else:
            players[1][0].send(b"Velg en sjampinjong")
            if startGame.input_champion('Player 2', 'blue', champions, player2, player1, read(players[1][0])):
                counter += 1
            else:
                counter = 0
    print('\n')

    # Match
    match = startGame.Match(
        startGame.Team([champions[name] for name in player1]),
        startGame.Team([champions[name] for name in player2])
    )
    match.play()


    # Print a summary
    startGame.print_match_summary(match)

print("aehfe")
main(heroes)
