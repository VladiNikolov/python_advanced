players = input().split(", ")

matrix = [input().split() for i in range(6)]
players_resting_dict = {player: 0 for player in players}

while True:
    row, col = [int(i) for i in input().strip("()").split(", ")]

    if players_resting_dict[players[0]]:
        players_resting_dict[players[0]] -= 1
        players.append(players.pop(0))
        continue

    position = matrix[row][col]

    if position == "E":
        print(f"{players[0]} found the Exit and wins the game!")
        break

    if position == "T":
        print(f"{players[0]} is out of the game! The winner is {players[1]}.")
        break

    if position == "W":
        print(f"{players[0]} hits a wall and needs to rest.")
        players_resting_dict[players[0]] += 1

    players.append(players.pop(0))