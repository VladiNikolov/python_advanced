from string import punctuation

def count_symbols(line):

    punctuations_symbols = set(punctuation)
    letters_count = 0
    punctuations_count = 0

    for symbol in line:
        if symbol.isalpha():
            letters_count += 1

        elif symbol in punctuations_symbols:
            punctuations_count += 1

    return letters_count, punctuations_count

with open("./text.txt", "r") as text_file, open("./output.txt", "w") as result_file:
    for index, line in enumerate(text_file):
        line = line.strip()
        letters, punctuations = count_symbols(line)
        result_file.write(f"Line {index + 1}: {line} ({letters})({punctuations})\n")