from collections import deque

pumps_count = int(input())
pumps = deque()
for _ in range(pumps_count):
    data_info = input().split()
    data_info = [int(i) for i in data_info]
    pumps.append(data_info)

for attempt in range(pumps_count):
    trunk = 0
    failed = False
    for element in pumps:
        petrol = element[0]
        distance = element[1]
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break