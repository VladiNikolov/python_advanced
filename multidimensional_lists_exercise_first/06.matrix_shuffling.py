def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(i) for i in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([int(i) for i in input().split()])

while True:
    line = input()
    if line == "END":
        break

    line_parts = line.split()

    if len(line_parts) != 5 or line_parts[0] != "swap":
        print("Invalid input!")
        continue

    row_index1, col_index1, row_index2, col_index2 = [int(i) for i in line_parts[1:]]


    if is_outside(row_index1, col_index1, rows, cols) or is_outside(row_index2, col_index2, rows, cols):
        print("Invalid input!")
        continue

    matrix[row_index1][col_index1], matrix[row_index2][col_index2] = matrix[row_index2][col_index2], matrix[row_index1][col_index1]

    for row in matrix:
        print(*row, sep=" ")