#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your UV Light Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_uv_light_v2 import BrickletUVLightV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    uvl = BrickletUVLightV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current UV-A
    uva = uvl.get_uva()
    print("UV-A: " + str(uva/10.0) + " mW/m²")

    # Get current UV-B
    uvb = uvl.get_uvb()
    print("UV-B: " + str(uvb/10.0) + " mW/m²")

    # Get current UV index
    uvi = uvl.get_uvi()
    print("UV Index: " + str(uvi/10.0))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
