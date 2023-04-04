#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your RGB LED Button Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_button import BrickletRGBLEDButton

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rlb = BrickletRGBLEDButton(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set light blue color
    rlb.set_color(0, 170, 234)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
