input_line = input().split()

result = []
while len(input_line) > 0:
    result.append(input_line.pop())
print(" ".join(result))