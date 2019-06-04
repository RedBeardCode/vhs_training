import json
import time
import requests


def set_led_color(color):
    """
    Setzt die Farbe der LED
    :param color: Farbe als Dict mit RGB-Wert z.B: {'red': 0, 'green': 0, 'blue': 0}
    """
    requests.post('http://192.168.4.1/pixel', data=json.dumps(color))


def create_color_gradient():
    """
    Berechnet einen fancy Farberverlauf
    :return: List mit RGB Farbwerten
    """
    colors = []
    step = 10
    for red, green in zip(range(255,-step, -step), range(0, 255, step)):
        colors.append({'red': red, 'green': green, 'blue': 0})
    for green, blue in zip(range(255,-step, -step), range(0, 255, step)):
        colors.append({'red': 0, 'green': green, 'blue': blue})
    for blue, red in zip(range(255,-step, -step), range(0, 255, step)):
        colors.append({'red': red, 'green': 0, 'blue': blue})
    return colors



if __name__ == '__main__':
    while True:
        for color in create_color_gradient():
            time.sleep(0.01)
            set_led_color(color)
