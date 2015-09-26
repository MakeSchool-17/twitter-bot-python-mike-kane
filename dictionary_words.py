import random

f = open('/Users/mikekane/Desktop/python_practice_files/words.txt', 'r')
word_list = f.readlines()


def random_sentences():
    sentence = ''
    word_count = 0
    sentence_length = random.randint(0, 30)
    while word_count != sentence_length:
        random_word = random.choice(word_list)
        sentence += random_word.rstrip() + ' '
        word_count += 1
    return sentence

print(random_sentences())
