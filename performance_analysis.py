import time
import re
import word_frequency as wf
import random


start = time.time()
source_text = 'Biggie_Smalls_Ready_To_Die.txt'


def hash_table(source_text):  # O(n) Complexity to create hash table
    # dictionary structure -- hash table of words, frequencies
    histogram = wf.histogram(source_text)
    return histogram


def associative_list(source_text):  # O(n) Complexity to create hash table
    # dictionary structure -- associative_list of words, frequencies
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

dictionary_histogram = hash_table(source_text)
associative_list_histogram = associative_list(source_text)


def get_random_vals_from_dict(histogram, num_random_words):
    randomly_selected_words = []
    for count in range(num_random_words):
        randomly_selected_words.append(random.choice(histogram.keys()))
    return (randomly_selected_words, time.time() - start)


def get_random_vals_from_ass_list(histogram, num_random_words):
    randomly_selected_words = []
    for count in range(num_random_words):
        random_word = random.choice(histogram)
        randomly_selected_words.append(random_word)
    return (randomly_selected_words, time.time() - start)


def get_ass_list_benchmark(histogram, num_trials):
    average_time = 0.0
    for count in range(num_trials):
        average_time += get_random_vals_from_ass_list(histogram, 10)[1]
    average_time /= float(num_trials)
    return average_time


print("Associative List avg time for 10000 trials:  " + str(get_ass_list_benchmark(associative_list_histogram, 20000)))


def get_dictionary_benchmark(histogram, num_trials):
    average_time = 0.0
    for count in range(num_trials):
        average_time += get_random_vals_from_dict(histogram, 10)[1]
    average_time /= float(num_trials)
    return average_time

print("Dictionary avg time for 10000 trials:  " + str(get_dictionary_benchmark(dictionary_histogram, 20000)))
# dict avg time = ~2.0s
