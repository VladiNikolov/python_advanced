rover_row, rover_col = 0, 0

size = 6
matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "E":
            rover_row, rover_col = row, col
    matrix.append(row_elements)

directions = input().split(", ")

water_found = False
metal_found = False
concrete_found = False

for direction in directions:

    if direction == "up":
        rover_row -= 1
    if direction == "down":
        rover_row += 1
    if direction == "left":
        rover_col -= 1
    if direction == "right":
        rover_col += 1

    if rover_row < 0:
        rover_row, rover_col = size - 1, rover_col
    if rover_row >= size:
        rover_row, rover_col = 0, rover_col
    if rover_col < 0:
        rover_row, rover_col = rover_row, size - 1
    if rover_col >= size:
        rover_row, rover_col = rover_row, 0

    cell_value = matrix[rover_row][rover_col]

    if cell_value == "W":
        water_found = True
        print(f"Water deposit found at ({rover_row}, {rover_col})")

    elif cell_value == "M":
        metal_found = True
        print(f"Metal deposit found at ({rover_row}, {rover_col})")

    elif cell_value == "C":
        concrete_found = True
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")

    elif cell_value == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if water_found and metal_found and concrete_found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")