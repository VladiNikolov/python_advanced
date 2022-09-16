parentheses = input()

stack = []
pairs = {
    "(": ")",
    "[": "]",
    "{": "}"
}

balanced = True
for element in parentheses:
    if element in "{[(":
        stack.append(element)

    elif not stack:
        balanced = False

    else:
        last_opening_bracket = stack.pop()
        if pairs[last_opening_bracket] != element:
            balanced = False
            break

    if not balanced:
        break
if not balanced or stack:
    print("NO")
else:
    print("YES")


