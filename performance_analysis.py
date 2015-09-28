import time
import re
import word_frequency as wf


start = time.time()
source_text = 'Biggie_Smalls_Ready_To_Die.txt'


# def hash_table(source_text):  # O(n) Complexity
#     # dictionary structure -- hash table of words, frequencies
#     histogram = wf.histogram(source_text)
#     return time.time() - start


# print(hash_table(source_text))
# benchmarks = 0.0
# for x in range(1000):
#     benchmarks += hash_table(source_text)
# benchmarks /= 1000
# print(benchmarks)


def associative_list(source_text):
    word_frequency = []
    file = open(source_text, 'r')
    text = file.read()
    text = text.replace('\n', ' ')
    pattern = re.compile("[^a-zA-Z0-9-']", re.I | re.M)
    full_lyrics = re.split(pattern, text)
    for lyric in full_lyrics:
        if lyric == '':
            full_lyrics.remove(lyric)

    lyric_types = set(full_lyrics)
    for lyric in lyric_types:
        counter = 1
        for token in full_lyrics:
            if lyric == token:
                counter += 1
        word_frequency.append((lyric, counter))

    return word_frequency

print(associative_list(source_text))
