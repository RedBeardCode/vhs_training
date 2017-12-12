"""
Temperatur lesen vom Multimeter VC960
"""

import urllib.request

def read_temperature(host):
    """
    Liest die Temperatur vom VC960 über das Netzwerk
    :param host: Adresse des Multimeters
    :return: Temperatur als Float
    """
    connection = urllib.request.urlopen(host)
    value_string = connection.read()
    return float(value_string)

print(__name__)
if __name__ == '__main__':
    temp = read_temperature('http://192.168.178.180:8000')
    print(temp)
    input("Press any Key")
