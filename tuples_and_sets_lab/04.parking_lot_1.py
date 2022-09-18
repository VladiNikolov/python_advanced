numbers = int(input())

parking_lot = [input().split(", ") for _ in range(numbers)]
parking_set = set()

for direction, car_number in parking_lot:
    if direction == "IN":
        parking_set.add(car_number)
    else:
        parking_set.remove(car_number)
if parking_set == set():
    print("Parking Lot is Empty")
else:
    [print(car_number) for car_number in parking_set]