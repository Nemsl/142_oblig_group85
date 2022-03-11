import socket
import json
import load_data

HOST = "127.0.0.1"
Local = "localhost"# The server's hostname or IP address
PORT = 65433  # The port used by the server
address = (HOST, PORT)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Local, PORT))

    s.sendall(json.dumps(load_data.getChamps()).encode())
    print('Received from server: ')
    while True:
        results = s.recv(2048).decode()
        print(results)
        if results != '':
            file1 = open("Result.txt", "w+")
            file1.write(results)
            print(file1.read())
            break