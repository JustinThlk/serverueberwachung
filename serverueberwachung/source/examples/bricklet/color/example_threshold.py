#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Color Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_color import BrickletColor

# Callback function for color reached callback
def cb_color_reached(r, g, b, c):
    print("Color [R]: " + str(r))
    print("Color [G]: " + str(g))
    print("Color [B]: " + str(b))
    print("Color [C]: " + str(c))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    c = BrickletColor(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    c.set_debounce_period(10000)

    # Register color reached callback to function cb_color_reached
    c.register_callback(c.CALLBACK_COLOR_REACHED, cb_color_reached)

    # Configure threshold for color "greater than 100, 200, 300, 400"
    c.set_color_callback_threshold(">", 100, 0, 200, 0, 300, 0, 400, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
