rows = int(input())

matrix = []
for _ in range(rows):
    row = [int(i) for i in input().split(", ")]
    matrix.extend(row)

print(matrix)