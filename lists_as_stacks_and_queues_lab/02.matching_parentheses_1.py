input_line = input()

stack = []

for index in range(len(input_line)):
    if input_line[index] == "(":
        stack.append(index)
    elif input_line[index] == ")":
        last_el = stack.pop()
        result = input_line[last_el] + input_line[index]
print(result)