import random


class Room:
    def __init__(self, player):
        self.enter_code = ''.join((random.choice('ABCDEFGHKLM5734921') for i in range(6)))

class Game:
    def __init__(self):
        pass

class Player:
    def __init__(self):
        pass