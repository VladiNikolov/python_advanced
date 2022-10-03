numbers_dictionary = {}

input_line = input()
while True:
    try:
        if input_line == "Search":
            break

        number_as_string = input_line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    input_line = input()

input_line = input()
while True:
    try:
        if input_line == "Remove":
            break

        searched = input_line
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    input_line = input()

input_line = input()
while True:
    try:
        if input_line == "End":
            break

        searched = input_line
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    input_line = input()

print(numbers_dictionary)
