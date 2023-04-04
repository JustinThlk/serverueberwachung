#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Linear Poti Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_linear_poti_v2 import BrickletLinearPotiV2

# Callback function for position callback
def cb_position(position):
    print("Position: " + str(position) + " %")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lp = BrickletLinearPotiV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register position callback to function cb_position
    lp.register_callback(lp.CALLBACK_POSITION, cb_position)

    # Set period for position callback to 0.25s (250ms) without a threshold
    lp.set_position_callback_configuration(250, False, "x", 0, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
