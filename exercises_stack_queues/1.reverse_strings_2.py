line = list(input())
result = []

while line:
    result.append(line.pop())
print(*result, sep="")
