input_string = input()

dict_numbers = {}

numbers = [float(i) for i in input_string.split()]

for number in numbers:
    if number not in dict_numbers:
        dict_numbers[number] = 0
    dict_numbers[number] += 1

for key, value in dict_numbers.items():
    print(f"{key} - {value} times")