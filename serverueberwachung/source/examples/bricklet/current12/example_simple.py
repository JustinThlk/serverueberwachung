#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Current12 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_current12 import BrickletCurrent12

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    c = BrickletCurrent12(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current current
    current = c.get_current()
    print("Current: " + str(current/1000.0) + " A")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
