#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Load Cell Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_load_cell import BrickletLoadCell

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lc = BrickletLoadCell(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current weight
    weight = lc.get_weight()
    print("Weight: " + str(weight) + " g")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
