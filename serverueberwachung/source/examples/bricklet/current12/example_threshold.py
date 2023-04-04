#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Current12 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_current12 import BrickletCurrent12

# Callback function for current reached callback
def cb_current_reached(current):
    print("Current: " + str(current/1000.0) + " A")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    c = BrickletCurrent12(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    c.set_debounce_period(10000)

    # Register current reached callback to function cb_current_reached
    c.register_callback(c.CALLBACK_CURRENT_REACHED, cb_current_reached)

    # Configure threshold for current "greater than 5 A"
    c.set_current_callback_threshold(">", 5*1000, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
