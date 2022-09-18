numbers = input().split()
numbers = [int(i) for i in numbers]

first_set = set()
second_set = set()
for _ in range(numbers[0]):
    current_number = int(input())
    if current_number not in first_set:
        first_set.add(current_number)

for _ in range(numbers[1]):
    current_number = int(input())
    if current_number not in second_set:
        second_set.add(current_number)

unique_elements = first_set.intersection(second_set)
[print(number) for number in unique_elements]
