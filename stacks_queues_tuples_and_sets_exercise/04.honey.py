from collections import deque

bees = deque([int(i) for i in input().split()])
nectars = [int(i) for i in input().split()]
operators = deque(input().split())
honey = 0
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        bees.appendleft(bee)
        continue
    if nectar == 0:
        continue

    operator = operators.popleft()
    honey += abs(operations[operator](bee, nectar))

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join([str(i) for i in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(i) for i in nectars])}")