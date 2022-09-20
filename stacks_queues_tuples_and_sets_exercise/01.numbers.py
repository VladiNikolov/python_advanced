first_set = set([int(i) for i in input().split()])
second_set = set([int(i) for i in input().split()])
number = int(input())

for _ in range(number):
    command_info = input().split()
    command = command_info[0]
    target_set = command_info[1]

    if command == "Add":
        if target_set == "First":
            first_set = first_set.union([int(i) for i in command_info[2:]])
        else:
            second_set = second_set.union([int(i) for i in command_info[2:]])
    elif command == "Remove":
        if target_set == "First":
            first_set = first_set.difference([int(i) for i in command_info[2:]])
        else:
            second_set = second_set.difference([int(i) for i in command_info[2:]])
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))
print(*sorted(first_set), sep= ", ")
print(*sorted(second_set), sep= ", ")

