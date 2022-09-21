rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(i) for i in input().split(", ")])
flatted_matrix = [current_element for element in matrix for current_element in element]

print(flatted_matrix)