numbers = int(input())

matrix = []
for _ in range(numbers):
    elements = [int(i) for i in input().split(", ")]
    even_elements = [i for i in elements if i % 2 == 0]
    matrix.append(even_elements)
print(matrix)