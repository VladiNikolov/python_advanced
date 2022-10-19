from collections import deque

seats = input().split(", ")
first_number = deque([int(x) for x in input().split(", ")])
second_number = deque([int(x) for x in input().split(", ")])

rotation = 0
new_seats_list = []

while len(new_seats_list) < 3 and rotation < 10:
    rotation += 1

    first_num = first_number.popleft()
    second_num = second_number.pop()
    letter = chr(first_num + second_num)

    first_option = str(first_num) + letter
    second_option = str(second_num) + letter

    if first_option in new_seats_list or second_option in new_seats_list:
        continue

    if first_option in seats:
        new_seats_list.append(first_option)
        continue

    if second_option in seats:
        new_seats_list.append(second_option)
        continue

    first_number.append(first_num)
    second_number.appendleft(second_num)

print(f"Seat matches: {', '.join(new_seats_list)}")
print(f"Rotations count: {rotation}")



