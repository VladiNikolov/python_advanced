rows = int(input())

matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split(", ")])
formatted_matrix = []
for element in matrix:
    for current_element in range(len(element)):
        formatted_matrix.append(element[current_element])
print(formatted_matrix)
