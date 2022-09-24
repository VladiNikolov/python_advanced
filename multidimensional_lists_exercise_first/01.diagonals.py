number = int(input())

matrix = []

for _ in range(number):
    matrix.append([int(i) for i in input().split(", ")])

primary_diagonal = []
for index in range(number):
    primary_diagonal.append(matrix[index][index])

secondary_diagonal = []
for index in range(number):
    secondary_diagonal.append(matrix[index][number - index - 1])

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")
