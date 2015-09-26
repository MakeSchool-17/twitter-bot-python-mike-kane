import random
import sys


def word_shuffler(wordList):
    tempWord = ''
    newWordList = []
    while True:
        if len(wordList) == 0:
            return newWordList
        else:
            tempWord = random.choice(wordList)
            newWordList.append(tempWord)
            wordList.remove(tempWord)

if __name__ == '__main__':
    args = sys.argv[1:]
    print(word_shuffler(args))
