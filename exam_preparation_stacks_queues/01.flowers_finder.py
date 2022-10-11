from collections import deque

def mark_words_letters(vowel, consonant, word_dict):
    result = False
    if vowel in word_dict:
        word_dict[vowel] = True
        result =  True

    if consonant in word_dict:
        word_dict[consonant] = True
        result = True
    return result

rose = {letter: False for letter in "rose"}
tulip = {letter: False for letter in "tulip"}
lotus = {letter: False for letter in "lotus"}
daffodil = {letter: False for letter in "daffodil"}


vowels_letter = deque(input().split())
consonants_letter = input().split()

found_flower = None
while vowels_letter and consonants_letter:
    vowel = vowels_letter.popleft()
    consonant = consonants_letter.pop()

    if mark_words_letters(vowel, consonant, rose):
        if all(rose.values()):
            found_flower = "rose"
            break

    if mark_words_letters(vowel, consonant, tulip):
        if all(tulip.values()):
            found_flower = "tulip"
            break

    if mark_words_letters(vowel, consonant, lotus):
        if all(lotus.values()):
            found_flower = "lotus"
            break

    if mark_words_letters(vowel, consonant, daffodil):
        if all(daffodil.values()):
            found_flower = "daffodil"
            break
if found_flower:
    print(f"Word found: {found_flower}")
else:
    print("Cannot find any word!")

if vowels_letter:
    result = " ".join(vowels_letter)
    print(f"Vowels left: {result}")
if consonants_letter:
    result = " ".join(consonants_letter)
    print(f"Consonants left: {result}")