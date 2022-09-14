input_line = input()

stack = []
for element in input_line:
    stack.append(element)

reversed_string = ""

while len(stack) > 0:
    reversed_string += stack.pop()

print(reversed_string)
