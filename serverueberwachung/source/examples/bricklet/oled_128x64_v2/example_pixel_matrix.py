#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your OLED 128x64 Bricklet
WIDTH = 128 # Columns
HEIGHT = 64 # Rows

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    oled = BrickletOLED128x64V2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Clear display
    oled.clear_display()

    # Draw checkerboard pattern
    pixels = []

    for row in range(HEIGHT):
        for column in range(WIDTH):
            pixels.append((row // 8) % 2 == (column // 8) % 2)

    oled.write_pixels(0, 0, WIDTH-1, HEIGHT-1, pixels)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
