"""
Поделить текст на слова и посчитать статистику биграмм, игнорируя размер букв. Вывести те биграммы, которые встречаются не реже чем 2 раза. 
Вывести в отсортированном по частотности порядке. 
Вывести символьные биграммы, готорые встречаются чаще 10 раз.
Вывести построчно.
"""

from collections import Counter
from string import punctuation

PUNC = set(punctuation)
LAST = -1
PREFIX = slice(None, -1)
SUFFIX = (1, None)
WORD_FREQ = 2
LETTER_FREQ = 11

def clear_word(word):
    while word[LAST] in PUNC:
        word = word[PREFIX]
    while word[0] in PUNC:
        word = word[SUFFIX]
    return word

def get_data(path='input.txt'):
    data = []
    with open(path, 'r') as f:
        for raw_line in f:
            line = raw_line.lower().split()
            for idx in range(len(line)):
                line[idx] = clear_word(line[idx])
            data.append(line)
    return data

def count_letter(word, letters):
    if len(word) == 1:
        if word.isalpha():
            letters[word] += 1
    elif word:
        for i in range(len(word) - 1):
            if word[i:i + 2].isalpha():
                letters[word[i:i + 2]] += 1

def count_bigrams(data):
    words, letters = Counter(), Counter()
    for line in data:
        if len(line) == 1:
            words[line[0]] += 1
            count_letter(line[0], letters)     
        elif line:
            for idx in range(len(line) - 1):
                words[' '.join([line[idx], line[idx + 1]])] += 1
                count_letter(line[idx], letters) 
            count_letter(line[LAST], letters) 
    return words, letters

def main():
    data = get_data()
    words, letters = count_bigrams(data)
    print("\n~~~~~Word's bigrams~~~~~\n")
    for word, freq in words.most_common():
        if freq >= WORD_FREQ:
            print(f'{word}: {freq}')
    print("\n~~~~~Letter's bigrams~~~~~\n")
    for pairs, freq in letters.most_common():
        if freq >= LETTER_FREQ:
            print(f'{pairs}: {freq}')

if __name__ =="__main__":
    main()
