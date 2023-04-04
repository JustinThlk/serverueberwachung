#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Digital In 4 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_digital_in_4 import BrickletIndustrialDigitalIn4

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    idi4 = BrickletIndustrialDigitalIn4(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current value as bitmask
    value_mask = idi4.get_value()
    print("Value Mask: " + format(value_mask, "04b"))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
