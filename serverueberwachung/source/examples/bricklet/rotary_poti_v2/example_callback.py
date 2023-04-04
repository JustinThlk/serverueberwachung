#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Rotary Poti Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_poti_v2 import BrickletRotaryPotiV2

# Callback function for position callback
def cb_position(position):
    print("Position: " + str(position) + " °")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rp = BrickletRotaryPotiV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register position callback to function cb_position
    rp.register_callback(rp.CALLBACK_POSITION, cb_position)

    # Set period for position callback to 0.25s (250ms) without a threshold
    rp.set_position_callback_configuration(250, False, "x", 0, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
