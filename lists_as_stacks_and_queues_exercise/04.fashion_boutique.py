clothes = input().split()
clothes = [int(i) for i in clothes]
racks_capacity = int(input())

current_racks_capacity = racks_capacity
racks_counter = 1

while clothes:
    piece_of_clothing = clothes[-1]

    if piece_of_clothing > current_racks_capacity:
        racks_counter += 1
        current_racks_capacity = racks_capacity
    else:
        current_racks_capacity -= piece_of_clothing
        clothes.pop()
print(racks_counter)

