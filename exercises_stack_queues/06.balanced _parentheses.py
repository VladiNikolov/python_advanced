parentheses = input()
parentheses_list = []

template = {
    "(": ")",
    "{": "}",
    "[": "]",
}
balanced_brackets = True
for element in parentheses:
    if element in "([{":
        parentheses_list.append(element)

    elif not parentheses_list:
        balanced_brackets = False

    else:
        last_opening_bracket = parentheses_list.pop()
        if template[last_opening_bracket] != element:
            balanced_brackets = False
            break

if not balanced_brackets or parentheses_list:
    print("NO")
else:
    print("YES")


