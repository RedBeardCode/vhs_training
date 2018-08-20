# -*- coding: utf-8 -*-
"""
Beispiel zum Umgang mit Dictionaries
"""

MONTHS = {
    1: 'Januar',
    2: 'Februar',
    3: 'März',
    4: 'April',
    5: 'Mai',
    6: 'Juni',
    7: 'Juli',
    8: 'August',
    9: 'September',
    10: 'Oktober',
    11: 'November',
    12: 'Dezember'
}

def replace_month(date_string):
    """
    Ersetz den Monatszahl eines Datumsstrings im Format(DD.MM.JJ) durch den
    Monatsnamen.
    """
    date_parts = date_string.split('.')
    date_parts[1] = MONTHS[int(date_parts[1])]
    date_string = '{0}. {1} {2}'.format(*date_parts)
    return date_string



print(replace_month('14.05.1979'))
print(replace_month('14.5.1979'))

