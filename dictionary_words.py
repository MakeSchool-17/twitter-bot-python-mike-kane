import random

f = open('/Users/mikekane/Desktop/python_practice_files/words.txt', 'r')
word_list = f.readlines()

# [brian] You forgot to close the file! It'll get closed when the script
# finishes, but until then this could use up a lot of resources! You could
# do

f.close()

# But forgetting to close files is an easy mistake to make, so python also
# lets you do:

with open('/Users/mikekane/Desktop/python_practice_files/words.txt') as f:
    word_list = f.readlines()

# and the file will be automatically closed when the program reaches this point.
# If you don't know what a context manager is yet don't worry too much about the
# syntax, but getting into the habit of never calling `open` without putting it
# in a with block is a good way to make your life easier.

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
