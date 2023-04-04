#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your RGB LED Button Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_button import BrickletRGBLEDButton

# Callback function for button state changed callback
def cb_button_state_changed(state):
    if state == BrickletRGBLEDButton.BUTTON_STATE_PRESSED:
        print("State: Pressed")
    elif state == BrickletRGBLEDButton.BUTTON_STATE_RELEASED:
        print("State: Released")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rlb = BrickletRGBLEDButton(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register button state changed callback to function cb_button_state_changed
    rlb.register_callback(rlb.CALLBACK_BUTTON_STATE_CHANGED, cb_button_state_changed)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
