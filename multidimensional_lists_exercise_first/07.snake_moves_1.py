rows, cols = [int(i) for i in input().split()]
word = input()

index = 0
for row in range(rows):
    elements = [None] * cols
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols-1, -1, -1)
    for col in range(start, end, step):
        elements[col] = word[index % len(word)]
        index += 1

    print("".join(elements))