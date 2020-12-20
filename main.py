from tuya import Tuya
import time
import pprint
import datetime


TUYA = Tuya()

pprint.pprint(TUYA.devices())


def __now(): 
    return datetime.datetime.now()


 
while True: 
    pprint.pprint (   TUYA.control('bfcd713c5bfb0355efdyyn', 0))
    time.sleep(10)
    pprint.pprint (   TUYA.control('bfcd713c5bfb0355efdyyn', 1))
    time.sleep(10)
