input_line = input()

stack = []
for index in range(len(input_line)):
    if input_line[index] == "(":
        stack.append(index)
    elif input_line[index] == ")":
        start_index = stack.pop()
        end_index = index
        print(input_line[start_index:end_index + 1])