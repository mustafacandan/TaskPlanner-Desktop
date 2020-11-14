# packages
import socket
import threading
import time
import yaml
# modules
from game import Game
from connection import Connection
from commands import read

credentials = yaml.safe_load(open('./credentials.yml'))
host = credentials['server']['host']
port = credentials['server']['port']

# socket initilization
sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    # listening port
    sck.bind((host, port))
    sck.listen(60)
    print(f"Server running on: {host} and port: {port}")
except Exception as e:
    raise SystemExit(
        f"We could not bind the server on host: {host} to port: {port}, because: {e}")

def on_new_client(client, connection):
    '''This function is called once on every new connection is made'''
    
    cnn = Connection(ip=connection[0], port=connection[1])
    print(f"The new connection was made from IP: {cnn.ip}!\nAll conenctions are listed:")
    print('\n'.join([f'\tip:{c.ip} : port:{c.port}' for c in Connection.get_all()]))

    # accepts incoming data from client
    while True:
        data = client.recv(64)
        command = read(data)
        
        if command == 'exit':
            break
        
    print(f"The client from ip: {cnn.ip}, and port: {cnn.port}, has gracefully diconnected!")
    client.close()


while True:
    try:
        # accepts new connections
        client, ip = sck.accept()
        # start new thread for new connection
        threading._start_new_thread(on_new_client, (client, ip))
    except KeyboardInterrupt:
        print(f"Gracefully shutting down the server!")
        break
    except Exception as e:
        print(f"Well I did not anticipate this: {e}")

sck.close()
