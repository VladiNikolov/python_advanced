numbers = int(input())

matrix = []

for row in range(numbers):
    matrix.append([int(i) for i in input().split()])

while True:
    current_line = input().split()
    if current_line[0] == "END":
        break
    command = current_line[0]
    row_index = int(current_line[1])
    col_index = int(current_line[2])
    number = int(current_line[3])

    if row_index < 0 or col_index < 0 or row_index >= len(matrix) or col_index >= len(matrix):
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row_index][col_index] += number
    elif command == "Subtract":
        matrix[row_index][col_index] -= number
for element in matrix:
    print(*element)