#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Dual AC Relay Bricklet

import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_dual_ac_relay import BrickletIndustrialDualACRelay

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    idacr = BrickletIndustrialDualACRelay(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Turn relays alternating on/off 10 times with 1 second delay
    for i in range(5):
        time.sleep(1)
        idacr.set_value(True, False)
        time.sleep(1)
        idacr.set_value(False, True)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
