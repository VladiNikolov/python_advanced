number = int(input())

matrix = []

for _ in range(number):
    matrix.append([int(i) for i in input().split()])

primary_diagonal = []
for index in range(number):
    primary_diagonal.append(matrix[index][index])

secondary_diagonal = []
for index in range(number):
    secondary_diagonal.append(matrix[index][number - index - 1])
difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(difference)