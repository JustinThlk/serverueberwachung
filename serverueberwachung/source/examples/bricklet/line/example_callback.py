#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Line Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_line import BrickletLine

# Callback function for reflectivity callback
def cb_reflectivity(reflectivity):
    print("Reflectivity: " + str(reflectivity))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    l = BrickletLine(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register reflectivity callback to function cb_reflectivity
    l.register_callback(l.CALLBACK_REFLECTIVITY, cb_reflectivity)

    # Set period for reflectivity callback to 1s (1000ms)
    # Note: The reflectivity callback is only called every second
    #       if the reflectivity has changed since the last call!
    l.set_reflectivity_callback_period(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
