players = input().split(", ")

matrix = []
for row in range(6):
    matrix.append(input().split())
players_resting = {player: 0 for player in players}

while True:

    position = input()
    row = int(position[1])
    col = int(position[4])

    if players_resting[players[0]]:
        players_resting[players[0]] -= 1
        players[0], players[1] = players[1], players[0]
        continue

    if matrix[row][col] == "E":
        print(f"{players[0]} found the Exit and wins the game!")
        break

    if matrix[row][col] == "T":
        print(f"{players[0]} is out of the game! The winner is {players[1]}.")
        break

    if matrix[row][col] == "W":
        print(f"{players[0]} hits a wall and needs to rest.")
        players_resting[players[0]] += 1

    players[0], players[1] = players[1], players[0]



