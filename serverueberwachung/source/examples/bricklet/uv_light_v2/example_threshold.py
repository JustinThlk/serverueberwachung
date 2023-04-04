#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your UV Light Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_uv_light_v2 import BrickletUVLightV2

# Callback function for UV index callback
def cb_uvi(uvi):
    print("UV Index: " + str(uvi/10.0))
    print("UV index > 3. Use sunscreen!")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    uvl = BrickletUVLightV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register UV index callback to function cb_uvi
    uvl.register_callback(uvl.CALLBACK_UVI, cb_uvi)

    # Configure threshold for UV index "greater than 3"
    # with a debounce period of 1s (1000ms)
    uvl.set_uvi_callback_configuration(1000, False, ">", 3*10, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
