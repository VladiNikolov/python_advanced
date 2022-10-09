from collections import deque

quantity_of_water = int(input())
people = deque()

while True:
    input_line = input()

    if input_line == "Start":
        break

    people.append(input_line)

while True:
    input_line = input()
    if input_line == "End":
        break

    line = input_line.split()
    if len(line) > 1:
        command = line[0]
        liters = int(line[1])
        quantity_of_water += liters
    else:
        liters = int(line[0])
        if quantity_of_water >= liters:
            person_name = people.popleft()
            print(f"{person_name} got water")
            quantity_of_water -= liters
        else:
            person_name = people.popleft()
            print(f"{person_name} must wait")

print(f"{quantity_of_water} liters left")
