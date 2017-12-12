import logging
from threading import Thread
from time import sleep

from serial import Serial

LOGGER = logging.getLogger(__name__)

LAST_TEMPERATURE = 0
LAST_PATTERN = b''

def read_temp_thread():
    global LAST_TEMPERATURE, LAST_PATTERN
    while True:
        sleep(0.5)
        LAST_TEMPERATURE, LAST_PATTERN = read_temp()

def get_last_temperature():
    return LAST_TEMPERATURE

def get_last_pattern():
    return LAST_PATTERN

#@app.task
def read_temp():
    """Read Temperature"""
    LOGGER.info("Read temperature")
    with Serial('/dev/ttyUSB0', 2400) as port:
        buffer = port.read(33)
        last_pattern_end = buffer.rfind(bytearray.fromhex('0D8A'))
        if last_pattern_end < 9:
            return 0, b''
        pattern = buffer[last_pattern_end-9:last_pattern_end+2]
        value_string = ''
        for byte in pattern[:5]:
            value_string += str(byte & 0X0F)
        return float(value_string) / 10.0, buffer
    return 0, b''


TEMP_THREAD = Thread(target=read_temp_thread)
TEMP_THREAD.start()
