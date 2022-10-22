matrix_rows, matrix_cols = [int(x) for x in input().split(", ")]
current_row, current_col = 0, 0
matrix = []

for row in range(matrix_rows):
    row_element = input().split()
    for col in range(matrix_cols):
        if row_element[col] == "Y":
            current_row = row
            current_col = col
    matrix.append(row_element)

input_command = input()

while input_command != "End":
    command_parts = input_command.split("-")
    direction = command_parts[0]
    steps = int(command_parts[1])

    matrix[current_row][current_col] = "x"


    if direction == "up":
        current_row, current_col = current_row - steps, current_col
    if direction == "down":
        current_row, current_col = current_row + steps, current_col
    if direction == "left":
        current_row, current_col = current_row, current_col - steps
    if direction == "right":
        current_row, current_col = current_row, current_col + steps

    if current_row < 0:
        current_row, current_col = matrix_rows - (steps), current_col
    if current_row >= matrix_rows:
        current_row, current_col = steps, current_col
    if current_col < 0:
        current_row, current_col = current_row, matrix_cols - (steps)

    if current_col >= matrix_cols:
        current_row, current_col = current_row, steps

    input_command = input()

matrix[current_row][current_col] = "Y"