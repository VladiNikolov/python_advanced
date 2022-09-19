input_line = input()

words_dict = {}
for element in input_line:
    if element not in words_dict:
        words_dict[element] = 0
    words_dict[element] += 1
for key, value in sorted(words_dict.items()):
    print(f"{key}: {value} time/s")
