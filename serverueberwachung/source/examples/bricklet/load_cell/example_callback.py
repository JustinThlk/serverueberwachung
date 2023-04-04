#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Load Cell Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_load_cell import BrickletLoadCell

# Callback function for weight callback
def cb_weight(weight):
    print("Weight: " + str(weight) + " g")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lc = BrickletLoadCell(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register weight callback to function cb_weight
    lc.register_callback(lc.CALLBACK_WEIGHT, cb_weight)

    # Set period for weight callback to 1s (1000ms)
    # Note: The weight callback is only called every second
    #       if the weight has changed since the last call!
    lc.set_weight_callback_period(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
