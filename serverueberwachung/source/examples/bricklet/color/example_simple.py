#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Color Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_color import BrickletColor

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    c = BrickletColor(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current color
    r, g, b, c_ = c.get_color()

    print("Color [R]: " + str(r))
    print("Color [G]: " + str(g))
    print("Color [B]: " + str(b))
    print("Color [C]: " + str(c_))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
