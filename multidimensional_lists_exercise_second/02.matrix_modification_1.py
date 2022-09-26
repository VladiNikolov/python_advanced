size_matrix = int(input())

matrix = []

for _ in range(size_matrix):
    matrix.append([int(i) for i in input().split()])

while True:
    line = input()
    if line == "END":
        break
    parts = line.split()
    command = parts[0]
    row, col, value = [int(i) for i in parts[1:]]

    if row < 0 or col < 0 or row >= size_matrix or col >= size_matrix:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value

    elif command == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=" ")