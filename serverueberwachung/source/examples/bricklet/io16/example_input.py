#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your IO-16 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_io16 import BrickletIO16

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    io = BrickletIO16(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current value from port A as bitmask
    value_mask_a = io.get_port("a")
    print("Value Mask (Port A): " + format(value_mask_a, "08b"))

    # Get current value from port B as bitmask
    value_mask_b = io.get_port("b")
    print("Value Mask (Port B): " + format(value_mask_b, "08b"))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
