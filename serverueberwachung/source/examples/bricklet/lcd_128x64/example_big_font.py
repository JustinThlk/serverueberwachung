#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your LCD 128x64 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_128x64 import BrickletLCD128x64

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lcd = BrickletLCD128x64(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Clear display
    lcd.clear_display()

    # Write "Hello World" with big 24x32 font
    lcd.draw_text(0, 0, lcd.FONT_24X32, lcd.COLOR_BLACK, "24x32")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
