#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Hall Effect Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_hall_effect import BrickletHallEffect

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    he = BrickletHallEffect(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current edge count without reset
    count = he.get_edge_count(False)
    print("Count: " + str(count))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
