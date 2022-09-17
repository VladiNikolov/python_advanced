number_of_guests = int(input())

guests_list = set()
arrivals_list = set()

for guest in range(number_of_guests):
    current_guest = input()
    guests_list.add(current_guest)

while True:
    arrived_guest = input()

    if arrived_guest == "END":
        break
    arrivals_list.add(arrived_guest)

missing_guest = guests_list.difference(arrivals_list)
print(len(missing_guest))

for guest in sorted(missing_guest):
    print(guest)