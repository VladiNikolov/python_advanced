number = int(input())

stack = []

while number > 0:
    input_line = input().split()
    command = input_line[0]

    if command == "1":
        added_number = int(input_line[1])
        stack.append(added_number)

    elif command == "2":
        if len(stack) > 0:
            stack.pop()

    elif command == "3":
        if len(stack) > 0:
            print(max(stack))

    elif command == "4":
        if len(stack) > 0:
            print(min(stack))

    number -= 1

result = []
while stack:
    result.append(stack.pop())
print(", ".join(map(str, result)))