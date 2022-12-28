from collections import Counter
from string import punctuation
PUNC = set(punctuation)

def get_data(path='input.txt'):
    data = []
    with open(path, 'r') as f:
        for raw_line in f:
            line = raw_line.lower().split()
            for idx in range(len(line)):
                while line[idx][-1] in PUNC:
                    line[idx] = line[idx][:-1]
                while line[idx][0] in PUNC:
                    line[idx] = line[idx][1:]
            data.append(line)
    return data

def count_letter(word, letters):
    if len(word) == 1:
        letters[word] += 1
    else:
        for i in range(len(word) - 1):
            letters[word[i:i + 1]] += 1


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
    print(count_bigrams(data))

if __name__ =="__main__":
    main()


