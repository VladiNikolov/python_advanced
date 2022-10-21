from collections import deque

pizza_orders = deque([int(i) for i in input().split(", ")])
employees_pizza = deque([int(i) for i in input().split(", ")])
pizza_count = 0
while pizza_orders and employees_pizza:

    pizza = pizza_orders.popleft()
    employees = employees_pizza.pop()

    if pizza <= 0:
        employees_pizza.append(employees)
        continue

    if pizza > 10:
        employees_pizza.append(employees)
        continue

    if pizza <= employees:
        continue

    if pizza > employees:
        pizza_count += pizza
        result = pizza - employees
        pizza_orders.appendleft(result)

        if len(employees_pizza) == 0:

            break
if len(pizza_orders) == 0:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza_count}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
if employees_pizza:
    print(f"Employees: {', '.join(map(str, employees_pizza))}")
