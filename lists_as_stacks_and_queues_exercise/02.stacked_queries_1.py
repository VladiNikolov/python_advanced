number = int(input())

stack = []

for _ in range(number):
    parts = [int(i) for i in input().split()]
    command = parts[0]

    if command == 1:
        added_number = parts[1]
        stack.append(added_number)

    elif command == 2:
        if stack:
            stack.pop()

    elif command == 3:
        if stack:
            print(max(stack))

    elif command == 4:
        if stack:
            print(min(stack))
stack.reverse()
print(", ".join(map(str, stack)))