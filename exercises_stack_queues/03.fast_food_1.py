from collections import deque

quantity_food = int(input())
orders_list = deque([int(i) for i in input().split()])

print(max(orders_list))
for _ in range(len(orders_list)):
    first_client_food = orders_list[0]
    if quantity_food >= first_client_food:
        quantity_food -= first_client_food
        orders_list.popleft()
    else:
        break

if len(orders_list) == 0:
    print("Orders complete")
else:
    orders_list = [str(i) for i in orders_list]
    remaining_orders = " ".join(orders_list)
    print(f"Orders left: {remaining_orders}")