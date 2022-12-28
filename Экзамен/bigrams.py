"""
Поделить текст на слова и посчитать статистику биграмм, игнорируя размер букв. Вывести те биграммы, которые не реже чем 2 раза. Вывести в отсортированном по частотности порядке. 
И вывести символьные биграммы, готорые встречаются чаще 10 раз.
Вывести построчечно.
"""

from collections import Counter
from string import punctuation

PUNC = set(punctuation)
LAST = -1
PREFIX = slice(None, -1)
SUFFIX = (1, None)
FIRST, SECOND = 0, 1

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
    else:
        for i in range(len(word) - 1):
            if word[i:i + 2].isalpha():
                letters[word[i:i + 2]] += 1

def count_bigrams(data):
    words = Counter()
    letters = Counter()
    for line in data:
        if len(line) == 1:
            words[line[0]] += 1
            count_letter(line[0], letters)                
        for idx in range(len(line) - 1):
            words[' '.join([line[idx], line[idx + 1]])] += 1
            count_letter(line[idx], letters) 
            count_letter(line[idx + 1], letters) 
    return words, letters

def main():
    data = get_data()
    words, letters = count_bigrams(data)
    print("\n~~~~~Word's bigrams~~~~~\n")
    for pair in words.most_common():
        if pair[1] >= 2:
            print(f'{pair[FIRST]}: {pair[SECOND]}')
    print("\n~~~~~Letter's bigrams~~~~~\n")
    for pair in letters.most_common():
        if pair[1] >= 10:
            print(f'{pair[FIRST]}: {pair[SECOND]}')

if __name__ =="__main__":
    main()
