import json
from logic import Game, Room

rooms = []


def operate(data):
    try:
        message = json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError('Invalid message from client')

    if message['command'] == 'create_room':
        player = message['player']
        room = Room(player)
        rooms.append(room)
        return 'enter_code', room.enter_code
    elif message['command'] == 'join_room':
        #  if there is a room with that code, player joins to the room
        pass
    elif message['command'] == 'find_room':
        # returns all the public rooms
        pass
    else:
        return None, None