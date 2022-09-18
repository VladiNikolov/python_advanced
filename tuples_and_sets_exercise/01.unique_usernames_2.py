input_lines = int(input())

unique_username = {input() for _ in range(input_lines)}
[print(username) for username in unique_username]
