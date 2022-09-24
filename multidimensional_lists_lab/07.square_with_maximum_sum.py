rows, cols = [int(i) for i in input().split(", ")]

matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

sum_all_elements = 0
max_row = 0
max_col = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        result = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
        if sum_all_elements < result:
            sum_all_elements = result
            max_row = row
            max_col = col
for row_i in range(max_row, max_row + 1 + 1):
    for col_i in range(max_col, max_col + 1 + 1):
        print(matrix[row_i][col_i], end= " ")
    print()
# print(matrix[max_row][max_col], matrix[max_row][max_col+1])
# print(matrix[max_row+1][max_col], matrix[max_row+1][max_col+1])

print(sum_all_elements)