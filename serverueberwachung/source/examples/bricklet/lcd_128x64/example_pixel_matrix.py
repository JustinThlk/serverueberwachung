#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your LCD 128x64 Bricklet
WIDTH = 128 # Columns
HEIGHT = 64 # Rows

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_128x64 import BrickletLCD128x64

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lcd = BrickletLCD128x64(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Clear display
    lcd.clear_display()

    # Draw checkerboard pattern
    pixels = []

    for row in range(HEIGHT):
        for column in range(WIDTH):
            pixels.append((row // 8) % 2 == (column // 8) % 2)

    lcd.write_pixels(0, 0, WIDTH-1, HEIGHT-1, pixels)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
