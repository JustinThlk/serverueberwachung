#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Load Cell Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_load_cell import BrickletLoadCell

# Callback function for weight reached callback
def cb_weight_reached(weight):
    print("Weight: " + str(weight) + " g")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lc = BrickletLoadCell(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 1 second (1000ms)
    lc.set_debounce_period(1000)

    # Register weight reached callback to function cb_weight_reached
    lc.register_callback(lc.CALLBACK_WEIGHT_REACHED, cb_weight_reached)

    # Configure threshold for weight "greater than 200 g"
    lc.set_weight_callback_threshold(">", 200, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
