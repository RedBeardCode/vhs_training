"""
Taschenrechner für die einfachen Grundrechenarten
Eingabe als String z.B 1+2
"""

from basic_arithmetic_operation import add, sub, multi, div


def calculator(calc_string):
    """
    Berechnt den als String übergeben Ausdruck
    """
    first = int(calc_string[0])
    second = int(calc_string[2])
    operator = calc_string[1]
    if operator == '+':
        result = add(first, second)

    return result


if __name__ == '__main__':
    calc_string = input('Bitte geben Sie eine Berechung ein')
    result = calculator(calc_string)
    print(result)


