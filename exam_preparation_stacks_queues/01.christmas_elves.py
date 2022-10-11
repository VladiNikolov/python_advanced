from collections import deque

elfs_energy = deque([int(i) for i in input().split()])
number_of_materials = [int(i) for i in input().split()]
used_energy = 0
gift_counter = 0
time_counter = 0

while elfs_energy and number_of_materials:

    while elfs_energy and elfs_energy[0] < 5:
        elfs_energy.popleft()

    if not elfs_energy:
        break

    energy = elfs_energy.popleft()
    material = number_of_materials.pop()
    time_counter += 1

    toys_created_count = 1
    spend_energy = material
    energy_factory = 1

    if time_counter % 3 == 0:
       toys_created_count = 2
       spend_energy *= 2

    if time_counter % 5 == 0:
        toys_created_count = 0
        energy_factory = 0

    if spend_energy <= energy:
        gift_counter += toys_created_count
        used_energy += spend_energy
        elfs_energy.append(energy - spend_energy + energy_factory)
    else:
        number_of_materials.append(material)
        elfs_energy.append(energy * 2)


print(f"Toys: {gift_counter}")
print(f"Energy: {used_energy}")

if elfs_energy:
    result = ", ".join(map(str, elfs_energy))
    print(f"Elves left: {result}")
else:
    result = ", ".join(map(str, number_of_materials))
    print(f"Boxes left: {result}")