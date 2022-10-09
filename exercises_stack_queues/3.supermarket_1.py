from collections import deque

people = deque()
input_line = input()

while input_line != "End":
    if input_line == "Paid":
        print("\n".join(people))
        people.clear()
    else:
        people.append(input_line)
    input_line = input()

print(f"{len(people)} people remaining.")