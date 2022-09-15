from collections import deque

quantity_of_food = int(input())
orders = input().split()
orders = [int(i) for i in orders]

orders_deque = deque()

for element in orders:
    orders_deque.append(element)
print(max(orders_deque))

while orders_deque:
    first_element = orders_deque[0]
    if quantity_of_food >= first_element:
        quantity_of_food -= first_element
        orders_deque.popleft()
    else:
        break
if len(orders_deque) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders_deque))}")
