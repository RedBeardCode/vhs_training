#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Einfacher Taschenrechner zum berechnen einfacher Ausdrücke
"""

from basic_arithmetic_operation import add, sub, multi, div

def calculator(calc_string):
    """
    Berechnet den als String gegeben Ausdruck
    :param calc_string: Berechnungsausdruck x(+-*/)y
    :return: Berechungsergebnis
    """
    split_plus = calc_string.split('+')
    if len(split_plus) == 2:
        return add(float(split_plus[0]), float(split_plus[1]))
    split_minus = calc_string.split('-')
    if len(split_minus) == 2:
        return sub(float(split_minus[0]), float(split_minus[1]))
    split_multi = calc_string.split('*')
    if len(split_multi) == 2:
        return multi(float(split_multi[0]), float(split_multi[1]))
    split_div = calc_string.split('/')
    if len(split_div) == 2:
        return div(float(split_div[0]), float(split_div[1]))


if __name__ == '__main__':
    calc_string = input('Bitte geben Sie eine Berechnung ein:')
    result = calculator(calc_string)
    print(result)
