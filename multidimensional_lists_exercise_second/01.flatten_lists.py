input_line = input().split("|")

result = []
for index in range(len(input_line) - 1, -1, -1):
    current_element = input_line[index].strip().split()
    result.extend(current_element)

print(*result)