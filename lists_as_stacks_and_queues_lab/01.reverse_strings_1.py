input_line = input()

stack = []

for i in range(len(input_line)):
    stack.append(input_line[i])

for index in range(len(stack)):
    print(stack.pop(), end="")