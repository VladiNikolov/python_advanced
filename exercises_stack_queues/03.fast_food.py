from collections import deque

quantity_of_the_food = int(input())
orders = deque([int(i) for i in input().split()])

print(max(orders))

while orders:
    client_order = orders[0]
    if quantity_of_the_food >= client_order:
        quantity_of_the_food -= client_order
        client_order = orders.popleft()
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    remaining_orders = " ".join(map(str, orders))
    print(f"Orders left: {remaining_orders}")


