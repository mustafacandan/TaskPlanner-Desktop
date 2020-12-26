class Player:
    def __init__(self, name, diceAmount):
        self.name = name
        self.diceAmount = diceAmount
player_list = []

def initPlayer(Player):
    player_list.append(Player)



ege = Player("ege", 5)



initPlayer(ege)

for player in player_list:
    print(player.name + str(player.diceAmount))
