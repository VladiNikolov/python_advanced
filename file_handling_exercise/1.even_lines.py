symbols = ["-", ",", ".", "!", "?"]

with open("./text.txt", "r") as text_file:
    for index, line in enumerate(text_file):
        if index % 2 == 0:
            reversed_word = (" ".join(line.strip().split()[::-1]))
            for symbol in symbols:
                reversed_word = reversed_word.replace(symbol, "@")
            print(reversed_word)
