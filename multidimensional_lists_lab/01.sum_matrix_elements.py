rows, columns = [int(i) for i in input().split(", ")]
matrix = []
result = 0
for i in range(rows):
    row = []
    for column in range(columns):
        row.append(column)
    matrix.append([int(i) for i in input().split(", ")])
for i in matrix:
    result += sum(i)
print(result)
print(matrix)
