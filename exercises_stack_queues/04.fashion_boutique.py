clothes = [int(i) for i in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
counter_rack = 1

while clothes:
    last_clothes = clothes[-1]
    if last_clothes > current_rack_capacity:
        counter_rack += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= last_clothes
        clothes.pop()

print(counter_rack)



