numbers = tuple(map(float, input().split()))
print(numbers)
unique_list = []
for number in numbers:
    if number not in unique_list:
        unique_list.append(number)


for number in unique_list:
    number_count = numbers.count(number)
    print(f"{number} - {number_count} times")