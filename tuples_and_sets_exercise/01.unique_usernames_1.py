input_lines = int(input())

unique_username = set()

for _ in range(input_lines):
    input_name = input()
    if input_name not in unique_username:
        unique_username.add(input_name)
for name in unique_username:
    print(name)