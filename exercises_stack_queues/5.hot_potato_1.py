from collections import deque

kids = deque(input().split())
number = int(input())

while len(kids) > 1:
    kids.rotate(-number)
    removed_kid = kids.pop()
    print(f"Removed {removed_kid}")

last_kid = kids.popleft()
print(f"Last is {last_kid}")
