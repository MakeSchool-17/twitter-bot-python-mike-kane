import re

from collections import defaultdict # [brian] I'll explain this part below


def histogram(source_text):  # generates histogram from data
    lyrics_histogram = {}
    # [brian] it's against convention to give your variables names like "file"
    # Try for a name like "source_file" or "file_". My editor highlights "file"
    # and makes this a little harder to read, and what if you want to call the
    # "file" function later in this method?
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

    # [brian] The above code could have been written:

    lyrics_histogram = defaultdict(int)
    for lyric in fullLyrics:
        lyrics_histogram[lyric] += 1

    # This pattern where you check whether a key exists and initialize it if
    # it doesn't is super common so python has tried to make it easier for
    # you to write.

    # The defaultdict constructor accepts a function, and when the key isn't
    # found calls that function instead of throwing an Exception. Here, `int`
    # is a function which returns 0, the default value.
    # https://docs.python.org/2/library/collections.html#collections.defaultdict

    return lyrics_histogram


def frequency(histogram, word):  # returns frequency of word in source text
    return histogram[word]


def num_unique_words(histogram):  # returns the total # of uinque words in data
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
