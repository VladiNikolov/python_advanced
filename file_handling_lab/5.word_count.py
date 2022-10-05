import re

words_dict = {}

with open("words.txt", "r") as words_file:
    all_words = words_file.read().split()
    words_dict = {word.lower(): 0 for word in all_words}

with open("input.txt", "r") as text_file:
    for line in text_file:
        all_line_words = re.findall("[a-zA-Z\']+", line)
        for word in all_line_words:
            word_lower = word.lower()
            if word_lower in words_dict:
                words_dict[word_lower] += 1

with open("output.txt", "w") as output_file:
    sorted_words = sorted(words_dict.items(), key=lambda x: -x[1])
    for words, value in sorted_words:
        output_file.write(f"{words} - {value}\n")