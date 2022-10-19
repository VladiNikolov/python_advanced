from collections import deque

seats = input().split(", ")
first_line = deque([int(i) for i in input().split(", ")])
second_line = [int(i) for i in input().split(", ")]

output_list = []
rotations = 0

while len(output_list) < 3 and rotations < 10:
    first_number = first_line[0]
    second_number = second_line[-1]
    result = chr(first_number + second_number)
    rotations += 1

    if str(first_number) + result in seats and str(first_number) + result not in output_list:
        output_list.append(str(first_number) + result)
        first_line.popleft()
        second_line.pop()
    elif str(second_number) + result in seats and str(second_number) + result not in output_list:
        output_list.append(str(second_number) + result)
        first_line.popleft()
        second_line.pop()
    else:
        first_line.append(first_line.popleft())
        current_element = second_line.pop()
        second_line.insert(0, current_element)

print(f"Seat matches: {', '.join(output_list)}")
print(f"Rotations count: {rotations}")
