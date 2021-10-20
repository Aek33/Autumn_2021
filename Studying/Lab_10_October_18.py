# Python modules
# Natzina Francis
"""
1. Create a module that takes in a nested list and an element
and returns the frequency of that element by nested level.
"""
# module Task 1

list_2 = []


def frequency_nested(list_, elem, lvl):
    nested_lvl = lvl
    count = 0
    for i in list_:
        if i == elem:
            count += 1
        elif isinstance(i, list):
            frequency_nested(i, elem, nested_lvl + 1)
    return list_2.append([count, nested_lvl])


def frequency(list_, elem):
    count = 0
    nested_lvl = 0
    for i in list_:
        if i == elem:
            count += 1
        elif isinstance(i, list):
            frequency_nested(list_, elem, nested_lvl)
    return list_2


# Task 2
"""
Task 2.	Write a module that takes the phonetic transcription of a Persian(Russian) word as an argument and 
returns the syllabified word based on the syllabic structure. In other word, put a period between syllables.

The division into syllables in Russian is based on the following rules:
1. The syllable forms a vowel
2. A syllable begins with a consonant that comes before a vowel
3. The letters ь, ъ, and й cannot be torn from the previous syllable
4. Voiceless consonants go to the next syllable
5. Voiced consonants followed by a noisy consonant go back to the previous syllable
6. Consonant letters that form one sound cannot be spread into different syllables.
One sound is formed by the combinations зж [ж:], тся, ться [ц:]
7. Doubled consonants in the middle of a word refer to the next syllable
"""

letters_dict = {"vowels": ("а", "у", "о", "и", "э", "ы", "я", "ю", "е", "ё"),
                "sonorous": ("й", "р", "л", "м", "н"), "rule_3": ("й", "ь")}


def syllables_decorator(fn):  # decorator to transform nested list of letters in pattern "syllable-...-syllable"
    def wrapper(*args):
        list_ = fn(*args)
        str_list = []
        for item in list_:
            str_syl = "".join(item)
            str_list.append(str_syl)
        word_ = "-".join(str_list)
        return word_

    return wrapper


def last_vowel(word):  # function for defining index of last vowel in word
    last_vowel_index = 0
    for letter in range(len(word) - 1, 0, -1):
        if word[letter] in letters_dict["vowels"]:
            last_vowel_index = letter
            break
    return last_vowel_index


@syllables_decorator
def to_syllables_Russian(word):
    word = word.lower()  # to avoid problems with lowercase/capital letters
    word = list(word)  # convert the word into char array
    last_vowel_index = last_vowel(word)  # index of last vowel
    syllables_list = []  # final list of all syllables
    const_count = 0  # for define consonants before vowel
    start = 0  # just for first loop
    vowel_count = 0  # just for first loop
    for i in range(len(word)):  # check for rule 3,
        if word[i] in letters_dict["vowels"]:
            vowel_count += 1
        if word[i] == "ъ":
            if vowel_count != 0:
                syllable = word[0: i + 1]
                syllables_list.append(syllable)
                start = i + 1
    for letter in range(start, len(word)):
        if word[letter] in letters_dict["vowels"]:
            if letter == last_vowel_index:  # end of word
                syllable = word[letter - const_count: len(word)]
                syllables_list.append(syllable)
                break  # if this is the last vowel in a word, there is no need to continue
            if word[letter + 1] in letters_dict["sonorous"]:  # check for rule 5
                if word[letter + 2] in letters_dict["rule_3"]:  # check for rule 3
                    syllable = word[letter - const_count: letter + 3]
                    syllables_list.append(syllable)
                    const_count = -2
                elif word[letter + 2] in letters_dict["vowels"]:
                    syllable = word[letter - const_count: letter + 1]
                    syllables_list.append(syllable)
                    const_count = 0
                else:
                    syllable = word[letter - const_count: letter + 2]
                    syllables_list.append(syllable)
                    const_count = -1
            else:
                syllable = word[letter - const_count: letter + 1]
                syllables_list.append(syllable)
                const_count = 0
        else:
            const_count += 1
    return syllables_list


def to_syllables_Russian_sentence(sentence):
    sentence = sentence.replace("[^\\а-яёА-ЯЁ ]", "")
    sentence = sentence.split()
    sentence_list = [to_syllables_Russian(word) for word in sentence]
    return sentence_list
