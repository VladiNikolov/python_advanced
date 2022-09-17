numbers = int(input())

unique = set()
for i in range(numbers):
    unique.add(input())
print("\n".join([unique_name for unique_name in unique]))
