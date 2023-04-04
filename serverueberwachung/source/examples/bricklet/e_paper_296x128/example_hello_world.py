#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your E-Paper 296x128 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_e_paper_296x128 import BrickletEPaper296x128

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ep = BrickletEPaper296x128(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Use black background
    ep.fill_display(ep.COLOR_BLACK)

    # Write big white "Hello World" in the middle of the screen
    ep.draw_text(16, 48, ep.FONT_24X32, ep.COLOR_WHITE, ep.ORIENTATION_HORIZONTAL,
                 "Hello World")
    ep.draw()

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
