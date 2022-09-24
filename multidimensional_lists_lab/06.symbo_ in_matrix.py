matrix_size = int(input())

matrix = []
is_found = False
for _ in range(matrix_size):
    matrix.append([i for i in input()])
symbol = input()

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{symbol} does not occur in the matrix")
