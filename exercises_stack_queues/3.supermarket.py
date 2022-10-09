from collections import deque
people = deque()

while True:
    input_line = input()
    if input_line == "End":
        break

    if input_line == "Paid":
        print(*people, sep="\n")
        people.clear()
    else:
        people.append(input_line)

print(f"{len(people)} people remaining.")