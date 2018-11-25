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
    pass

def is_cell_alive(field, x, y):
    """
    Überprüft ob eine Zelle am leben ist. Beachte das Spielfeld hat einen Rand, der beachtet werden muss
    :param field: Spielfeld
    :param x: Nummer der Spalte
    :param y: Nummer der Zeile
    :return: True wenn die Zelle am leben ist
    """
    pass

def set_cell_value(field, x, y, value):
    """
    Setzt den Wert einer Zelle auf den angegeben wert. Beachte das Spielfeld hat einen Rand, der beachtet werden muss
    :param field: Spielfeld
    :param x: Nummer der Spalte
    :param y: Nummer der Zeile
    :param value: Neuer Wert der Zelle
    """
    pass

def get_field_size(field):
    """
    Ermittelt die Größe des Spielfelds
    :param field: Spielfeld
    :return: Tuple aus Anzahl der Spalten und Anzahl der Zeilen
    """
    pass

def should_cell_be_alive(field, x, y):
    """
    Bestimmt ob eine Zelle in der nächsten Runde am leben sein soll oder nicht
    :param field: Spielfeld
    :param x: Nummer der Spalte
    :param y: Nummer der Zeile
    :return: True wenn die Zelle am leben sein soll
    """
    pass

def fill_field_with_live(field, num_cells):
    """
    Befüllt das Spielfeld mit lebenden Zellen an zufälligen Position
    :param field: Spielfeld
    :param num_cells: Anzahl der lebenden Zellen
    """
    pass

def evolution(field):
    """
    Berechnet einen Evolutionzyklus für das Spielfeld und erstellt ein neues Spielfeld für das Ergebnis des Zylkus.
    :param field: Spielfeld
    :return: Neues Spielfeld mit den neuen lebenden Zellen
    """
    pass

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
