number = int(input())

table_dict = {}

for _ in range(number):
    current_line = input().split()
    for element in current_line:
        if element not in table_dict:
            table_dict[element] = 0
        else:
            continue
for key in table_dict.keys():
    print(key)