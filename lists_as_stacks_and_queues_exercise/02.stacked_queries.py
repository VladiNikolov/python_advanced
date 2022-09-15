number = int(input())

stack = []
for i in range(number):
    command = input()
    command = command.split()
    current_command = int(command[0])

    if current_command == 1:
        added_number = int(command[1])
        stack.append(added_number)

    elif current_command == 2 and stack:
        stack.pop()

    elif current_command == 3 and stack:
        print(max(stack))

    elif current_command == 4 and stack:
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))
print(", ".join(reversed_stack))
