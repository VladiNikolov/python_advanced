rows, cols = [int(i) for i in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([int(i) for i in input().split()])

while True:
    line = input()
    if line == "END":
        break

    line_info = line.split()
    command = line_info[0]
    if command != "swap" or len(line_info) != 5:
        print("Invalid input!")
        continue

    row_index1 = int(line_info[1])
    col_index1 = int(line_info[2])
    row_index2 = int(line_info[3])
    col_index2 = int(line_info[4])

    if row_index1 < 0 or row_index2 < 0 or col_index1 < 0 or col_index2 < 0 \
            or row_index1 >= rows or row_index2 >= rows or col_index1 >= cols or col_index2 >= cols:
        print("Invalid input!")
        continue

    matrix[row_index1][col_index1], matrix[row_index2][col_index2] = matrix[row_index2][col_index2], matrix[row_index1][col_index1]

    for row in matrix:
        print(*row, sep=" ")