#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from requests import get

"""
Frägt das aktuelle Wetter für eine gegebene Stadt von
https://openweathermap.org ab
"""

API_KEY = 'xxxx'

CITY = 'Altenkirchen,de'


def get_weather(city):
    """
    Frägt das Wetter für die gegebene Stadt ab

    :param city: Stadt für die das Wetter abgefragt
                 wird (Stadtname, Länderkürzel)
    :returns: Wetterbeschreibung in JSON
    """
    url = 'http://api.openweathermap.org/data/2.5/' \
          'weather?q={}&appid={}&units=metric'.format(
            city,
            API_KEY
    )
    response = get(url)
    return response.json()


if __name__ == '__main__':
    WEATHER = get_weather(CITY)
    print(WEATHER)
