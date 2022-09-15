from collections import deque

water_quantity = int(input())
people = deque()

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input()

    if command == "End":
        break

    elif command.startswith("refill"):
        data_info = command.split()
        refilled_water = data_info[1]
        water_quantity += int(refilled_water)
    else:
        person = people.popleft()
        water_wanted = int(command)

        if water_wanted <= water_quantity:
            print(f"{person} got water")
            water_quantity -= water_wanted
        else:
            print(f"{person} must wait")

print(f"{water_quantity} liters left")