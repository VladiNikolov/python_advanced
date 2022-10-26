size = int(input())
row, col = 0, 0
matrix = []
for current_row in range(size):
    row_elements = [i for i in input()]
    for element in row_elements:
        if element == "S":
            row, col = current_row, row_elements.index(element)
    matrix.append(row_elements)

next_row, next_col = 0, 0
food = 0
while True:
    direction = input()
    matrix[row][col] = "."

    if direction == "up":
        next_row, next_col = row - 1, col
    if direction == "down":
        next_row, next_col = row + 1, col
    if direction == "left":
        next_row, next_col = row, col - 1
    if direction == "right":
        next_row, next_col = row, col + 1

    if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
        print("Game over!")
        break
    else:
        row, col = next_row, next_col

    if matrix[row][col] == "-":
        matrix[row][col] = "."

    elif matrix[row][col] == "*":
        food += 1
        matrix[row][col] = "."

    elif matrix[row][col] == "B":
        matrix[row][col] = "."
        for row_index in range(size):
            for col_index in range(size):
                if matrix[row_index][col_index] == "B":
                    row, col = row_index, col_index
                    continue
    if food >= 10:
        matrix[row][col] = "S"
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food}")
for row in matrix:
    print("".join(row))

