from pprint import pprint
from random import randint
from time import sleep
DEATH = '.'
ALIVE = 'x'


def get_empty_field(size_x, size_y):
    """
    Erzeugt ein Feld aus toten Zellen mit size_x Spalten und size_y Zeilen und einen Rand um das Feld mit toten Zeilen
    :param size_x: Anzahl an Spalten
    :param size_y: Anzahl an Zeilen
    :returns: Ein Spielfeld mit toten Zeilen
    """
    field = []
    for j in range(size_y + 2):
        line = [DEATH] * (size_x + 2)
        field.append(line)
    return field

def is_cell_alive(field, x, y):
    """
    Überprüft ob eine Zelle am leben ist. Beachte das Spielfeld hat einen Rand, der beachtet werden muss
    :param field: Spielfeld
    :param x: Nummer der Spalte
    :param y: Nummer der Zeile
    :return: True wenn die Zelle am leben ist
    """
    is_alive = field[y+1][x+1] == ALIVE
    return field[y+1][x+1] == ALIVE

def set_cell_value(field, x, y, value):
    """
    Setzt den Wert einer Zelle auf den angegeben wert. Beachte das Spielfeld hat einen Rand, der beachtet werden muss
    :param field: Spielfeld
    :param x: Nummer der Spalte
    :param y: Nummer der Zeile
    :param value: Neuer Wert der Zelle
    """
    field[y+1][x+1] = value

def get_field_size(field):
    """
    Ermittelt die Größe des Spielfelds
    :param field: Spielfeld
    :return: Tuple aus Anzahl der Spalten und Anzahl der Zeilen
    """
    size_y = len(field) - 2
    size_x = len(field[0]) - 2
    return size_x, size_y

def should_cell_be_alive(field, x, y):
    """
    Bestimmt ob eine Zelle in der nächsten Runde am leben sein soll oder nicht
    :param field: Spielfeld
    :param x: Nummer der Spalte
    :param y: Nummer der Zeile
    :return: True wenn die Zelle am leben sein soll
    """
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if is_cell_alive(field, x+i, y+j):
                count += 1
    if is_cell_alive(field, x, y) and (count == 3 or count == 4):
        return ALIVE
    elif count == 3:
        return ALIVE
    return DEATH

def fill_field_with_live(field, num_cells):
    """
    Befüllt das Spielfeld mit lebenden Zellen an zufälligen Position
    :param field: Spielfeld
    :param num_cells: Anzahl der lebenden Zellen
    """
    count = 0
    size_x, size_y = get_field_size(field)
    while count < num_cells:
        x = randint(0, size_x - 1)
        y = randint(0, size_y - 1)
        if not is_cell_alive(field, x, y):
            count += 1
            set_cell_value(field, x, y, ALIVE)


def evolution(field):
    """
    Berechnet einen Evolutionzyklus für das Spielfeld und erstellt ein neues Spielfeld für das Ergebnis des Zylkus.
    :param field: Spielfeld
    :return: Neues Spielfeld mit den neuen lebenden Zellen
    """
    size_x, size_y = get_field_size(field)
    new_field = get_empty_field(size_x, size_y)
    for y in range(size_y):
        for x in range(size_x):
            if should_cell_be_alive(field, x, y) == ALIVE:
                set_cell_value(new_field, x, y, ALIVE)
    return new_field

def display_field(field, delete_old_field):
    """
    Gibt das Spielfeld auf der Konsole aus
    :param field:
    :return:
    """
    size_x, size_y = get_field_size(field)
    for j in range(size_y+2):
        field[j] = ''.join(field[j])
    str_field = '\n'.join(field)
    if delete_old_field:
        print("\033[F" * (size_y+3))
    print(str_field)


if __name__ == '__main__':
    NUM_X = 60
    NUM_Y = 40
    NUM_CELLS = 150
    # Anlegen des Basisspielfelds
    field = get_empty_field(NUM_X, NUM_Y)
    fill_field_with_live(field, NUM_CELLS)
    # Evolutionszyklen berechnen
    for i in range(5):
        display_field(field, i>0)
        field = evolution(field)
        sleep(1)
