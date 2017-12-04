#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementierung der 4 Grundrechenarten
"""

def add(x ,y):
    """Berechnet die Summe"""
    return x + y

def sub(x, y):
    """Berechnet die Differenz"""
    return x - y

def multi(x, y):
    """Brechnet das Produkt"""
    return x * y

def div(x, y):
    """Berechnet den Quotienten"""
    return x / y


if __name__ == '__main__':
    print('Summe:', add(1, 1))
    print('Differenz: ', sub(5, 2))
    print('Produkt:', multi(6, 7))
    print('Differenz:', div(5, 2))
