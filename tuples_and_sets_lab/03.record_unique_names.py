numbers = int(input())

names_list = []
for element in range(numbers):
    name = input()
    names_list.append(name)

unique_elements = set()
for element in names_list:
    unique_elements.add(element)

for element in unique_elements:
    print(element)
