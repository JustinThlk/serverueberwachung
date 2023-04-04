#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Color Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_color import BrickletColor

# Callback function for color callback
def cb_color(r, g, b, c):
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

    # Register color callback to function cb_color
    c.register_callback(c.CALLBACK_COLOR, cb_color)

    # Set period for color callback to 1s (1000ms)
    # Note: The color callback is only called every second
    #       if the color has changed since the last call!
    c.set_color_callback_period(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
