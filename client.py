import socket
import argparse

parser = argparse.ArgumentParser(
    description="This is the client for the multi threaded socket server!")
parser.add_argument('--host', metavar='host', type=str,
                    nargs='?', default='127.0.0.1')
parser.add_argument('--port', metavar='port',
                    type=int, nargs='?', default=5001)
args = parser.parse_args()

print(f"Connecting to server: {args.host} on port: {args.port}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
    try:
        sck.connect((args.host, args.port))
    except Exception as e:
        raise SystemExit(
            f"We have failed to connect to host: {args.host} on port: {args.port}, because: {e}")

    while True:
        msg = input("What do we want to send to the server?: ")
        sck.sendall(msg.encode('utf-8'))
        if msg == 'exit':
            print("Client is saying goodbye!")
            break
        data = sck.recv(64)
        print(f"The server's response was: {data.decode()}")
