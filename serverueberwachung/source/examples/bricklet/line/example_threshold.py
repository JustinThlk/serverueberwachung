#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Line Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_line import BrickletLine

# Callback function for reflectivity reached callback
def cb_reflectivity_reached(reflectivity):
    print("Reflectivity: " + str(reflectivity))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    l = BrickletLine(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 1 second (1000ms)
    l.set_debounce_period(1000)

    # Register reflectivity reached callback to function cb_reflectivity_reached
    l.register_callback(l.CALLBACK_REFLECTIVITY_REACHED, cb_reflectivity_reached)

    # Configure threshold for reflectivity "greater than 2000"
    l.set_reflectivity_callback_threshold(">", 2000, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
