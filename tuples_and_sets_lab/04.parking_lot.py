number = int(input())

unique_car_numbers = set()
for i in range(number):
    direction, car_number = input().split(", ")

    if direction == "IN":
        unique_car_numbers.add(car_number)

    elif direction == "OUT":
        unique_car_numbers.remove(car_number)

if len(unique_car_numbers) > 0:
    for plate in unique_car_numbers:
        print(plate)
else:
    print("Parking Lot is Empty")
