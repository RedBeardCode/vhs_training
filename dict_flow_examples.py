# -*- coding: utf-8 -*-
"""
Beispiel zum Umgang mit Dictionaries und Kontrollstrukturen
"""

from string_examples import read_file

WORD_COUNTS = {}

def count_word_appearance():
    """
    Zählt die Häufigkeit der einzelnen Wörter im Textbeispiel
    """
    global WORD_COUNTS
    lines = read_file()
    for line in lines:
        for special_char in ['.', ',', ';', '!', '?', '\n', "'"]:
            line = line.replace(special_char, '')
        for word in line.split(' '):
            if len(word) == 0:
                continue
            count = WORD_COUNTS.get(word, 0)
            count += 1
            WORD_COUNTS[word] = count


def get_number_of_words():
    """
    Gibt die Anzahl der Wörter im Textbeispiel zurück
    """
    return len(WORD_COUNTS)

def get_most_mentioned_word():
    """
    Gibt das meist genutze Wort und dessen Häufigkeit zurück
    """
    max_count = -1
    max_word = ''
    for word in WORD_COUNTS:
        if WORD_COUNTS[word] > max_count:
            max_count = WORD_COUNTS[word]
            max_word  = word
    return max_word, max_count

def sorted_output():
    """
    Gibt die Worthäufigkeit in alphabetischer Reihenfolge aus
    """
    for word in sorted(WORD_COUNTS):
        print('{0}: {1}'.format(word, WORD_COUNTS[word]))


def descending_output():
    """
    Gibt die Worthäufigkeit in absteigender Reihenfolge aus
    """
    for word in sorted(WORD_COUNTS,
                       key=lambda word: WORD_COUNTS[word],
                       reverse=True):
        print('{0}: {1}'.format(word, WORD_COUNTS[word]))
