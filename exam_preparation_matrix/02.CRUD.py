matrix = []

for _ in range(6):
    input_line = input().split()
    matrix.append(input_line)

position = input()
row = int(position[1])
col = int(position[4])

input_command = input()

while input_command != "Stop":
    command_parts = input_command.split(", ")
    command = command_parts[0]
    direction = command_parts[1]

    if direction == "up":
        row -= 1
    if direction == "down":
        row += 1
    if direction == "left":
        col -= 1
    if direction == "right":
        col += 1

    if command == "Create":
        value = command_parts[2]
        if matrix[row][col] == ".":
            matrix[row][col] = value

    if command == "Update":
        value = command_parts[2]
        if matrix[row][col] != ".":
            matrix[row][col] = value

    if command == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."

    if command == "Read":
        if matrix[row][col] != ".":
            print(matrix[row][col])

    input_command = input()

for row in matrix:
    print(" ".join(row))

# [print(*row) for row in matrix]