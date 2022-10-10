clothes = [int(i) for i in input().split()]
rack_capacity = int(input())

rack_counter = 1
current_rack_capacity = rack_capacity

while len(clothes) > 0:
    last_clothes = clothes[-1]

    if last_clothes > current_rack_capacity:
        rack_counter += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= last_clothes
        clothes.pop()
print(rack_counter)