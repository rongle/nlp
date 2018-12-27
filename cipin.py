# -*- coding: utf-8 -*-
from fenci import fenci
import operator

def cipin():
    wordlist = fenci()
    word_frequency = {}
    for word in wordlist:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    word_frequency = sorted(word_frequency.items(), key = operator.itemgetter(1))
    print(len(word_frequency))
    with open('./corpus/word_frequency.txt', 'w', encoding='utf-8') as fw:
        fw.write(str(word_frequency))

if __name__ == '__main__':
    cipin()