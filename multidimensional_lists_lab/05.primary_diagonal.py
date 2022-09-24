number = int(input())

matrix = []
for row in range(number):
    matrix.append([int(i) for i in input().split()])
primary_diagonal = 0
for index in range(number):
    primary_diagonal += matrix[index][index]
print(primary_diagonal)
