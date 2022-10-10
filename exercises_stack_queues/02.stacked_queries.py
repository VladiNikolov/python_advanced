number = int(input())

stack = []

for _ in range(number):
    input_line = input().split()
    if input_line[0] == "1":
        number = int(input_line[1])
        stack.append(number)

    elif input_line[0] == "2":
        if stack:
            stack.pop()

    elif input_line[0] == "3":
        if stack:
            print(max(stack))

    elif input_line[0] == "4":
        if stack:
            print(min(stack))

print(*reversed(stack), sep=", ")