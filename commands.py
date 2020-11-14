import json

def read(data):
    message = json.loads(data)
    print(message['player'])