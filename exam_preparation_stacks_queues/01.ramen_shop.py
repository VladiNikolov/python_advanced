from collections import deque

bowls_with_ramen = deque([int(i) for i in input().split(", ")])
customer = deque([int(i) for i in input().split(", ")])

while bowls_with_ramen and customer:

    current_bowls = bowls_with_ramen.pop()
    current_customer = customer.popleft()

    if current_bowls == current_customer:
        continue

    if current_bowls > current_customer:
        result = current_bowls - current_customer
        bowls_with_ramen.append(result)

    if current_bowls < current_customer:
        result = abs(current_customer - current_bowls)
        customer.appendleft(result)

if len(customer) == 0:
    print("Great job! You served all the customers.")
else:
    print("Out of ramen! You didn't manage to serve all customers.")

if bowls_with_ramen:
    print(f"Bowls of ramen left: {', '.join(map(str, bowls_with_ramen))}")
if customer:
    print(f"Customers left: {', '.join(map(str, customer))}")