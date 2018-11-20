#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from requests import get

"""
Frägt Wettervorhersage für eine gegebene Stadt von
https://openweathermap.org ab
"""

API_KEY = 'xxx'

CITY = 'Altenkirchen,de'


def get_weather_forecast(city):
    """
    Frägt die Wettervorhersage für die gegebene Stadt ab

    :param city: Stadt für die das Wetter abgefragt
                 wird (Stadtname, Länderkürzel)
    :returns: Wetterbeschreibung in JSON
    """
    url = 'http://api.openweathermap.org/data/2.5/' \
          'forecast?q={}&appid={}&units=metric'.format(
            city,
            API_KEY
    )
    response = get(url)
    return response.json()

def get_daily_extrema(forecast):
    """
    Sucht aus der 3-stündigen Vorhersage alle Werte für einen Tag und
    sucht das Tagesminimum und -maximum
    :param forecast: Liste mit Vorhersage dicts
    :return: Dict mit Datumsstring als Key und einen Dict mit Tagesmininum
    key min und Tagesmaximum key max
    """
    min_dict = {}
    max_dict = {}
    for hourly_forecast in forecast:
        key = hourly_forecast['dt_txt'].split()[0]
        add_list_value(hourly_forecast['main']['temp_min'], key, min_dict)
        add_list_value(hourly_forecast['main']['temp_max'], key, max_dict)
    daily_dict = {}
    for key in min_dict:
        temp_min = min(min_dict[key])
        temp_max = max(max_dict[key])
        daily_dict[key] = {'min': temp_min, 'max': temp_max}
    return daily_dict

def add_list_value(value, key, wrapping_dict):
    """
    Fügt einen neue Wert an die List an, die als Wert mit den gegeben Key
    in einem Dict verwendet wird ein
    :param value: Neuer Wert
    :param key: Schlüssel der Liste
    :param wrapping_dict: Dict in der die Liste gespeichert ist
    """
    key_list = wrapping_dict.get(key, [])
    key_list.append(value)
    wrapping_dict[key] = key_list

def will_there_be_frost(daily_weather):
    """
    Durchsucht die tägliche Vorhersage und gibt True zurück wenn es frost gibt
    :param daily_weather: Dict mit den täglichen min und max Temperaturen
    :return: True wenn es frost gibt
    """
    for date in daily_weather:
        if daily_weather[date]['min'] < 0:
            return True
    return False


if __name__ == '__main__':
    WEATHER = get_weather_forecast(CITY)
    DAILY_DICT = get_daily_extrema(WEATHER['list'])
    print(will_there_be_frost(DAILY_DICT))
    print(DAILY_DICT)
