expressions = input()
index_open_bracket = []

for index in range(len(expressions)):
    current_element = expressions[index]

    if current_element == "(":
        index_open_bracket.append(index)
    elif current_element == ")":
        last_open_bracket = index_open_bracket.pop()
        substring = expressions[last_open_bracket : index + 1]
        print(substring)
