#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Line Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_line import BrickletLine

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    l = BrickletLine(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current reflectivity
    reflectivity = l.get_reflectivity()
    print("Reflectivity: " + str(reflectivity))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
