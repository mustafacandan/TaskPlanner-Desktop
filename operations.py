import json
from logic import Game, Room

rooms = []


def operate(data):
    message = json.loads(data)

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