numbers = int(input())

unique = set()
for i in range(numbers):
    name = input()
    unique.add(name)
for name in unique:
    print(name)