#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your RGB LED Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led import BrickletRGBLED

import colorsys
import time

SECONDS_PER_ROUND = 1.5
COLORS_PER_ROUND = 256

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rl = BrickletRGBLED(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    print("Press ctrl+c to exit")

    while True:
        for i in range(COLORS_PER_ROUND):
            r, g, b = colorsys.hsv_to_rgb(1.0*i/COLORS_PER_ROUND, 1, 0.1) # Calculate color
            rl.set_rgb_value(int(r*255), int(g*255), int(b*255)) # Set color

            time.sleep(SECONDS_PER_ROUND/COLORS_PER_ROUND) # Wait for next color change

    ipcon.disconnect()
