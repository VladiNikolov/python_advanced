numbers_of_guests = int(input())

regular_list = set()
vip_list = set()

for guest in range(numbers_of_guests):
    current_input = input()
    if current_input[0].isdigit():
        vip_list.add(current_input)
    else:
        regular_list.add(current_input)
arrived_guest = input()
while arrived_guest != "END":
    if arrived_guest[0].isdigit():
        vip_list.remove(arrived_guest)
    else:
        regular_list.remove(arrived_guest)

    arrived_guest = input()
number_not_arrivals = len(regular_list) + len(vip_list)
print(number_not_arrivals)
union_list = regular_list | vip_list
print("\n".join(sorted(union_list)))

