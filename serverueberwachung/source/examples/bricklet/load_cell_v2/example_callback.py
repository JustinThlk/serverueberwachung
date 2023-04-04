#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Load Cell Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_load_cell_v2 import BrickletLoadCellV2

# Callback function for weight callback
def cb_weight(weight):
    print("Weight: " + str(weight) + " g")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lc = BrickletLoadCellV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register weight callback to function cb_weight
    lc.register_callback(lc.CALLBACK_WEIGHT, cb_weight)

    # Set period for weight callback to 1s (1000ms) without a threshold
    lc.set_weight_callback_configuration(1000, False, "x", 0, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
