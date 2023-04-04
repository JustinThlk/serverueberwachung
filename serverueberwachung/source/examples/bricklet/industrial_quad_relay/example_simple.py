#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Quad Relay Bricklet

import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_quad_relay import BrickletIndustrialQuadRelay

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    iqr = BrickletIndustrialQuadRelay(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Turn relays alternating on/off 10 times with 100 ms delay
    for i in range(10):
        time.sleep(0.1)
        iqr.set_value(1 << 0)
        time.sleep(0.1)
        iqr.set_value(1 << 1)
        time.sleep(0.1)
        iqr.set_value(1 << 2)
        time.sleep(0.1)
        iqr.set_value(1 << 3)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
