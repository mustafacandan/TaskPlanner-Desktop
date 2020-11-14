import socket
import json
import yaml

credentials = yaml.safe_load(open('./credentials.yml'))
host = credentials['server']['host']
port = credentials['server']['port']

print(f"Connecting to server: {host} on port: {port}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
    try:
        sck.connect((host, port))
    except Exception as e:
        raise SystemExit(
            f"We have failed to connect to host: {host} on port: {port}, because: {e}")

    while True:
        # msg = input("What do we want to send to the server?: ")
        data = {
            'player': '0001',
            'command': 'create_room'
        }
        msg = json.dumps(data)
        sck.sendall(msg.encode('utf-8'))
        if msg == 'exit':
            print("Client is saying goodbye!")
            break
        data = sck.recv(64)
        print(f"The server's response was: {data.decode()}")
