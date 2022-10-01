input_line = list(input())

stack = []
while len(input_line) > 0:
    stack.append(input_line.pop())

print(*stack, sep="")
# print("".join(stack))
