#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Distance US Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_us import BrickletDistanceUS

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    dus = BrickletDistanceUS(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current distance value
    distance = dus.get_distance_value()
    print("Distance Value: " + str(distance))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
