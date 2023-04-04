#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Dual Button Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_dual_button_v2 import BrickletDualButtonV2

# Callback function for state changed callback
def cb_state_changed(button_l, button_r, led_l, led_r):
    if button_l == BrickletDualButtonV2.BUTTON_STATE_PRESSED:
        print("Left Button: Pressed")
    elif button_l == BrickletDualButtonV2.BUTTON_STATE_RELEASED:
        print("Left Button: Released")

    if button_r == BrickletDualButtonV2.BUTTON_STATE_PRESSED:
        print("Right Button: Pressed")
    elif button_r == BrickletDualButtonV2.BUTTON_STATE_RELEASED:
        print("Right Button: Released")

    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    db = BrickletDualButtonV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register state changed callback to function cb_state_changed
    db.register_callback(db.CALLBACK_STATE_CHANGED, cb_state_changed)

    # Enable state changed callback
    db.set_state_changed_callback_configuration(True)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
