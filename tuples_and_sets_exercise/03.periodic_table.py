number = int(input())

table_set = set()
for _ in range(number):
    current_elements = input().split()
    for elements in current_elements:
        if elements not in table_set:
            table_set.add(elements)
for element in table_set:
    print(element)