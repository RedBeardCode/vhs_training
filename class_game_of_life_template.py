from pprint import pprint
from random import randint
from time import sleep

FIELD = {}

class Cell:

    def __init__(self, x, y, alive):
        """
        Speichert die position und den Status as private Variablen
        :param x:
        :param y:
        :param alive:
        """
        pass

    def should_be_alive(self, field):
        """
        Bestimmt ob die Zell im nächsten Zug am Leben sein soll
        :param field: Spielfeld
        :return: True wenn die Zelle leben soll
        """
        pass

    def awake(self):
        """Erweckt die Zelle zum Leben"""
        pass

    def give_new_born_neighbours(self, field):
        """
        Gibt eine Liste der Nachbaren zurück die am Leben sein sollen
        :param field: Spielfeld
        :return: List mit lebenden Nachbaren zellen
        """
        pass

    def get_position(self):
        """
        Gibt die Position der Zelle als Tuple zurück
        """
        pass



def fill_field_with_live(num_cells, start_size, field):
    """
    Befüllt das Spielfelde mit lebenden Startzellen
    :param num_cells: Anzahl der Startzellen
    :param start_size: Größe des quadratischen Startspielfelds
    :param field: Leeres Spielfeld
    """
    pass

def evolution(field):
    """
    Berechnet einen Evolutionzyklus für das Spielfeld und erstellt ein neues Spielfeld für das Ergebnis des Zylkus.
    :param field: Spielfeld
    :return: Neues Spielfeld mit den neuen lebenden Zellen
    """
    pass

def display_field(field, size_x, size_y, delete_old_field):
    """
    Gibt das Spielfeld auf der Konsole aus
    """
    display = []
    for _ in range(size_y):
        line = ['.'] * size_x
        display.append(line)
    for x, y in field.keys():
        if x >= 0 and x < size_x and y >= 0 and y < size_y:
            display[y][x] = 'x'
    for j in range(size_y):
        display[j] = ''.join(display[j])
    str_field = '\n'.join(display)

    if delete_old_field:
        print("\033[F" * (size_y+1))
    print(str_field)


if __name__ == '__main__':
    START_SIZE = 6
    NUM_CELLS = 10
    # Anlegen des Basisspielfelds
    field = {}
    fill_field_with_live(NUM_CELLS, START_SIZE, field)
    # Evolutionszyklen berechnen
    for i in range(15):
        display_field(field, START_SIZE, START_SIZE, i>0)
        field = evolution(field)
        sleep(1)
