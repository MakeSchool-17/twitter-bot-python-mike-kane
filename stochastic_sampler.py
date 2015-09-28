import word_frequency as wf
import random

histogram = wf.histogram('Biggie_Smalls_Ready_To_Die.txt')


def stochastic_sampler(histogram):
    totalLyricsList = []
    for word, total_use in histogram.items():
        for x in range(total_use):
            totalLyricsList.append(word)
    return random.choice(totalLyricsList)


def percentage_checker(word, wordList):
    word_count = 0
    actual_frequency = 0.0
    for w in wordList:
        if w == word:
            word_count += 1
    actual_frequency = float(word_count) / len(wordList)
    return actual_frequency

testList = []
for x in range(100):
    if x < 13:
        testList.append('a')
    else:
        testList.append('b')


def probability_checker(histogram, count):
    random_word_chosen = []
    percentage_of_appearances = []
    a_f = 0.0   # actual frequency
    e_f = 0.0   # expected frequency
    total_word_count = wf.total_word_count("Biggie_Smalls_Ready_To_Die.txt")
    for instance in range(count):
        random_word_chosen.append(stochastic_sampler(histogram))

    for word in random_word_chosen:
        a_f = percentage_checker(word, random_word_chosen)
        e_f = wf.frequency(histogram, word) / float(total_word_count)
        percentage_of_appearances.append((word, "expected: {}  actual:  {}".format(e_f, a_f)))

    return percentage_of_appearances


def make_it_readable(data):
    for line in data:
        print(line[0], line[1])

print(make_it_readable(probability_checker(histogram, 10000)))
