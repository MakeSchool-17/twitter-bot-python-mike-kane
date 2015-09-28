import re


def histogram(source_text):  # generates histogram from data
    lyrics_histogram = {}
    file = open(source_text, 'r')
    text = file.read()
    text = text.replace('\n', ' ')
    pattern = re.compile("[^a-zA-Z0-9-']", re.I | re.M)
    fullLyrics = re.split(pattern, text)
    for lyric in fullLyrics:
        if lyric == '':
            fullLyrics.remove(lyric)

    for lyric in fullLyrics:
        if lyric not in lyrics_histogram:
            lyrics_histogram[lyric] = 1
        else:
            lyrics_histogram[lyric] += 1

    return lyrics_histogram


def frequency(histogram, word):  # returns frequency of word in source text
    return histogram[word]


def unique_words(histogram):  # returns the total # of uinque words in data
    return len(histogram)


def total_word_count(file):
    totalWordCount = 0
    f = open(file, 'r')
    text = f.read()
    text = text.replace('\n',  ' ')
    pattern = re.compile("[^a-zA-Z0-9-']", re.I | re.M)
    fullLyrics = re.split(pattern, text)
    for lyric in fullLyrics:
        if lyric == '':
            fullLyrics.remove(lyric)

    for lyric in fullLyrics:
        totalWordCount += 1

    return totalWordCount
# histogram = histogram('Biggie_Smalls_Ready_To_Die.txt')

# print("histogram of biggie smalls lyrics:  ")
# print(histogram)
# print('Total words used across biggie smalls album "Ready To Die":'
#       + str(unique_words(histogram)))
