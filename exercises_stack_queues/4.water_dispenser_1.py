from collections import deque

people = deque()
all_water_in_dispenser = int(input())

input_line = input()
while input_line != "Start":
    people.append(input_line)
    input_line = input()

input_line = input()
while input_line != "End":
    line = input_line.split()
    if len(line) == 2:
        command = line[0]
        liters = int(line[1])
        all_water_in_dispenser += liters
    else:
        liters = int(line[0])
        if all_water_in_dispenser >= liters:
            person_name = people.popleft()
            print(f"{person_name} got water")
            all_water_in_dispenser -= liters
        else:
            person_name = people.popleft()
            print(f"{person_name} must wait")
    input_line = input()


print(f"{all_water_in_dispenser} liters left")