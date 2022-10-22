size = int(input())
racing_number = input()

matrix = []
distance = 0
for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
row, col = 0, 0

while True:
    direction = input()

    if direction == "End":
        matrix[row][col] = "C"
        print(f"Racing car {racing_number} DNF.")
        break

    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    if matrix[row][col] == ".":
        distance += 10

    elif matrix[row][col] == "T":
        distance += 30
        for row_index in range(size):
            for col_index in range(size):
                if matrix[row_index][col_index] == "T":
                    row, col = row_index, col_index
                    matrix[row][col] = "."
    elif matrix[row][col] == "F":
        matrix[row][col] = "C"
        distance += 10
        print(f"Racing car {racing_number} finished the stage!")
        break

print(f"Distance covered {distance} km." )
for row in matrix:
    print(f"{''.join(row)}")