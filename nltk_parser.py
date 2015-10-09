import codecs
from nltk import word_tokenize
import re
import sys

remove_thanks_pattern = re.compile(r'\nThanks(.|\n(?!\n))+(\n)*"[^"]+".*',
                                   re.IGNORECASE)
remove_narration_pattern = re.compile(r'\[[^\]]+\]\s*', re.IGNORECASE |
                                      re.MULTILINE)


def check_if_roman_numeral(word):
    roman_numerals = ["I", "V", "X", "L", "C", "M"]
    if len(word) == 1:
        return False
    for letter in word:
        if letter not in roman_numerals:
            return False
    return True


def parse_and_tokenize(source_text):
    source_text = re.sub(remove_thanks_pattern, ' ', source_text)
    source_text = re.sub(remove_narration_pattern, ' ', source_text)
    tokenized_text = word_tokenize(source_text)
    for word in tokenized_text:
        if check_if_roman_numeral(word):
            tokenized_text.remove(word)
    return tokenized_text


if __name__ == '__main__':
    files_to_be_parsed = sys.argv[1:-1]
    output_file = sys.argv[-1]
    print(output_file)
    finished_parsed_corpus = ''
    for file in files_to_be_parsed:
        with codecs.open(file, 'r', encoding='utf-8') as f:
            source_text = f.read()
            parsed_text = parse_and_tokenize(source_text)
            parsed_text.sort()

            for word in parsed_text:
                finished_parsed_corpus += word + ' '

    with codecs.open(output_file, 'w', encoding='utf-8') as w:
        w.write(finished_parsed_corpus)
