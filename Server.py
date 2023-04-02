import socket
from  threading import Thread
import time
import os

IP_ADDRESS = "127.0.0.1"
port = 8080
SERVER = None
BUFFER_SIZE = 4096
clients = {}
is_dir_exists = os.path.isdir("shard_files")
print(is_dir_exists)
if(not is_dir_exists):
    os.makedirs("shared_files")


def acceptConnections():
    global SERVER
    global clients
    while True:
        client, addr = SERVER.accept()
        print(client,addr)
        client_name = client.recv(4096).decode().lower()
        clients[client_name] = {
            "client": client,
            "address": addr,
            "connected_with": "",
            "file_name": "",
            "file_size": 4096
        }
    print(f"connection established with {client_name}")
    thread = Thread(target = handleClient, args = (client, client_name))
    thread.start()


def setup():
    print("IP Messenger")
    global port
    global IP_ADDRESS
    global SERVER
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, port))
    SERVER.listen(100)
    print("Server is waiting for incoming connections")
    acceptConnections()
setup_thread = Thread(target = setup)
setup_thread.start()
