#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Distance US Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_us import BrickletDistanceUS

# Callback function for distance value callback
def cb_distance(distance):
    print("Distance Value: " + str(distance))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    dus = BrickletDistanceUS(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register distance value callback to function cb_distance
    dus.register_callback(dus.CALLBACK_DISTANCE, cb_distance)

    # Set period for distance value callback to 0.2s (200ms)
    # Note: The distance value callback is only called every 0.2 seconds
    #       if the distance value has changed since the last call!
    dus.set_distance_callback_period(200)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
