input_lines = input().split()

stack = []
for i in range(len(input_lines)):
    stack.append(input_lines.pop())
print(*stack)
