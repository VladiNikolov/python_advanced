numbers_file = open("numbers.txt", "r")
sum_numbers = 0

for number in numbers_file:
    sum_numbers += int(number)
print(sum_numbers)