class Player:
    def __init__(self, name):
        self.name = name
        self.points = []

players = []
players_count = int(input("Сколько игроков?"))

for i in range(players_count):
    players.append(Player(input("Input name player"+str(i+1))))

strin = ''
for i in players:
    print(players.name)