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

    # [brian] The above could also be written as:

    result = []
    while wordList:
        index = random.randrange(len(wordList))
        result.append(wordList.pop(index))
    return result

    # saving you from having to use a temporary variable.

    # In particular, the "while True" loop is very scary, I usually
    # avoid writing "while True" unless I really mean for something
    # to loop forever. Saying something like "while wordList" makes it explicit
    # you intend for the loop to end at some point and that you're going to be
    # messing with wordList inside the body of the loop.

    # It could also be written:

    random.shuffle(wordList)
    return wordList

    # although that doesn't have quite the same effect, it modifies the wordList
    # which was passed in and therefore isn't quite as pretty.


if __name__ == '__main__':
    args = sys.argv[1:]
    print(word_shuffler(args))
