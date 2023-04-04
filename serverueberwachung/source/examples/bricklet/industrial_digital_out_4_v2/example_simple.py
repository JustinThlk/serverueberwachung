#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Digital Out 4 Bricklet 2.0

import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_digital_out_4_v2 import BrickletIndustrialDigitalOut4V2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ido4 = BrickletIndustrialDigitalOut4V2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set channels alternating high/low 10 times with 100 ms delay
    for i in range(10):
        time.sleep(0.1)
        ido4.set_value([True, False, False, False])
        time.sleep(0.1)
        ido4.set_value([False, True, False, False])
        time.sleep(0.1)
        ido4.set_value([False, False, True, False])
        time.sleep(0.1)
        ido4.set_value([False, False, False, True])

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
