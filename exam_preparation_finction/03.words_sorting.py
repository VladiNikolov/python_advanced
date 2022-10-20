def words_sorting(*args):
    def calculate_words_value(word):
        return sum(ord(x) for x in word)

    words_dict = {word: calculate_words_value(word) for word in args}

    total_words_value = sum(words_dict.values())
    if total_words_value % 2 == 0:
        result = sorted(words_dict.items())
    else:
        result = sorted(words_dict.items(), key=lambda x: (x[1]), reverse=True)

    return "\n".join(f"{key} - {value}" for (key, value) in result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
