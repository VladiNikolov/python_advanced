rows, cols = [int(i) for i in input().split(", ")]

matrix = []
for _ in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

result = 0
for row in range(rows):
    for col in range(cols):
        result += matrix[row][col]
print(result)
print(matrix)
