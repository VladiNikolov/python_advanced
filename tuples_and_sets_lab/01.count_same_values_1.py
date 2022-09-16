numbers = input().split()
numbers = tuple(map(float, numbers))

unique_dict = {}
for number in numbers:
    if number not in unique_dict:
        unique_dict[number] = 1
    else:
        unique_dict[number] += 1
for key, value in unique_dict.items():
    print(f"{key} - {value} times")