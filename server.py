import socket
import argparse
import threading
import time
import weakref
from game import Game
from connection import Connection
from commands import read

parser = argparse.ArgumentParser( description="Liars Dice Server")
parser.add_argument('--host', metavar='host', type=str, nargs='?', default='127.0.0.1')
parser.add_argument('--port', metavar='port', type=int, nargs='?', default=5001)
args = parser.parse_args()

sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(f"Server running on: {args.host} and port: {args.port}")

try:
    sck.bind((args.host, args.port))
    sck.listen(60)
except Exception as e:
    raise SystemExit(
        f"We could not bind the server on host: {args.host} to port: {args.port}, because: {e}")

def on_new_client(client, connection):
    cnn = Connection(ip=connection[0], port=connection[1])
    print(f"THe new connection was made from IP: {cnn.ip}, and port: {cnn.port}!")
    print('All conenctions are listed:')
    for c in Connection.get_all():
        print(f'\tip:{c.ip} : port:{c.port}')
    while True:
        msg = client.recv(64)
        if msg.decode() == 'exit':
            break
        else:
            read(msg.decode())
        print(f"The client said: {msg.decode()}")
        # reply = f"You told me: {msg.decode()}"
        # client.sendall(reply.encode('utf-8'))
    print(
        f"The client from ip: {cnn.ip}, and port: {cnn.port}, has gracefully diconnected!")
    client.close()


while True:
    try:
        client, ip = sck.accept()
        threading._start_new_thread(on_new_client, (client, ip))
    except KeyboardInterrupt:
        print(f"Gracefully shutting down the server!")
    except Exception as e:
        print(f"Well I did not anticipate this: {e}")
    time.sleep(0.5)

sck.close()
