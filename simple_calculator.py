#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Einfacher Addierer
"""

def add(x,y):
    """
    Addiert die beiden übergebenen Zahlen
    :param x: Erste Zahl
    :param y: Zweite Zahl
    :return: Summe der beiden Zahlen
    """
    return x + y

#Zahlen vom Benutzer abfragen
x_str = input('Bitte geben Sie die erste Zahl ein:  ')
y_str = input('Bitte geben Sie die zweite Zahl ein: ')

#Wichtig: Texte in Zahlen umwandeln
x = float(x_str)
y = float(y_str)

sum = add(x,y)

print(sum)
