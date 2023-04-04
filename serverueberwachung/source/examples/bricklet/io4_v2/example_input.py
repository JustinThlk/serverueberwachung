#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your IO-4 Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_io4_v2 import BrickletIO4V2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    io = BrickletIO4V2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current value
    value = io.get_value()

    print("Channel 0: " + str(value[0]))
    print("Channel 1: " + str(value[1]))
    print("Channel 2: " + str(value[2]))
    print("Channel 3: " + str(value[3]))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
