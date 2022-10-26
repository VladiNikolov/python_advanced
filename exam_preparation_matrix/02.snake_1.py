def moves(direction, row, col):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1

def is_outside(row, col, size):
    return row < 0 or row >= size or col < 0 or col >= size


size = int(input())
row, col = 0, 0
matrix = []

for current_row in range(size):
    row_elements = [i for i in input()]
    for element in row_elements:
        if element == "S":
            row, col = current_row, row_elements.index(element)
    matrix.append(row_elements)

next_row, next_col = row, col
food = 0

while True:
    direction = input()
    matrix[row][col] = "."
    next_row, next_col = moves(direction, next_row, next_col)

    if is_outside(next_row, next_col, size):
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
                    next_row, next_col = row_index, col_index
                    matrix[next_row][next_col] = "."
                    continue
    if food >= 10:
        matrix[row][col] = "S"
        print("You won! You fed the snake.")
        break
print(f"Food eaten: {food}")
for row in matrix:
    print("".join(row))

