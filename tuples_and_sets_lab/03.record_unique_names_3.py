numbers = int(input())
unique_names = {input() for n in range(numbers)}
[print(name) for name in unique_names]
