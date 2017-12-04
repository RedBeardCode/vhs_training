#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Beispiele zum Umgang mit Listen
"""

def odd_list(num=10):
    """
    Erstellt eine Liste mit ungeraden Zahlen
    """
    return list(range(1, num, 2))


def descending_even_list(num=20):
    """
    Erstellt eine Liste mit geraden Zahlen in absteigender Reihenfolge
    """
    return list(range(2*num -2, -1, -2))


def multiples_list(multiple=5, num=5, len_list=100):
    """
    Selektiert die Vielfachen aus einer Liste heraus
    """
    whole_list = list(range(len_list))
    return whole_list[multiple:num*multiple+1:multiple]


def sequence_list():
    """
    Erstelle eine Liste bestehend aus 5 mal 0 und 5 mal 1
    """
    zeros = [0] * 5
    ones = [1] * 5
    return zeros + ones


def repeat_sequence_list(num=5):
    """
    Wiederholt die Sequenzeliste
    """
    return sequence_list() * 5


def add_value_to_list(list, value):
    """
    Hängt ein Element an eine Liste an.
    Untersuche nach dem Aufruf der Funktion die übergebene Liste
    """
    new_list = list + [value]
    list.append(value)
    return new_list


def remove_element(list, index=3):
    """
    Entfernt ein Element aus einer Liste
    """
    list.pop(index)
