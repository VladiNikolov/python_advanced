from collections import deque

my_deque = deque()
while True:
    command = input()
    if command == "End":
        print(f"{len(my_deque)} people remaining.")
        break
    elif command == "Paid":
        while my_deque:
            print(my_deque.popleft())
    else:
        my_deque.append(command)
