from collections import deque

kids_string = input()
tosses_count = int(input())

kids_deque = deque(kids_string.split())

current_count = 0

while len(kids_deque) > 1:
    current_count += 1

    kid = kids_deque.popleft()
    if current_count < tosses_count:
        kids_deque.append(kid)
    else:
        print(f"Removed {kid}")
        current_count = 0

print(f"Last is {kids_deque.popleft()}")