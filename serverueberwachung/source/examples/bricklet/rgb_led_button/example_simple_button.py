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

    # Get current button state
    state = rlb.get_button_state()

    if state == rlb.BUTTON_STATE_PRESSED:
        print("State: Pressed")
    elif state == rlb.BUTTON_STATE_RELEASED:
        print("State: Released")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
