#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Distance US Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_us import BrickletDistanceUS

# Callback function for distance value reached callback
def cb_distance_reached(distance):
    print("Distance Value: " + str(distance))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    dus = BrickletDistanceUS(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    dus.set_debounce_period(10000)

    # Register distance value reached callback to function cb_distance_reached
    dus.register_callback(dus.CALLBACK_DISTANCE_REACHED, cb_distance_reached)

    # Configure threshold for distance value "smaller than 200"
    dus.set_distance_callback_threshold("<", 200, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
