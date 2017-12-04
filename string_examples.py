
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Beispiele zum Umgang mit Strings
"""

def read_file(filename='textbeispiel.txt'):
    """
    Liest eine Textdatei und und gibt eine Liste der Zeilen zurück
    """
    txt_file = open(filename, 'r', encoding='utf-8')
    lines = txt_file.readlines()
    txt_file.close()
    return lines


def count_lines():
    """
    Zählt die Anzahl von Zeilen
    """
    lines = read_file()
    return len(lines)


def capitalize_heading():
    """
    Wandelt die Überschrift in Grossbuchstaben um
    """
    lines = read_file()
    # String sind unveränderlich, deshalb erstellt upper einen neuen String
    lines[0] = lines[0].upper()
    return lines


def count_words():
    """
    Zählt die Wörter
    """
    lines = read_file()
    text = ''.join(lines)
    words = text.split()
    return len(words)


def replace_word(word='Glocke', new_word='Klimbim'):
    """
    Ersetzt ein Wort durch ein anderes
    """
    lines = read_file()
    text = ''.join(lines)
    # String sind unveränderlich, deshalb erstellt replace einen neuen String
    text = text.replace(' ' + word + ' ', ' ' + new_word + ' ')
    text = text.replace('\n' + word + ' ', '\n' + new_word + ' ')
    text = text.replace(' ' + word + '\n', ' ' + new_word + '\n')
    return text
