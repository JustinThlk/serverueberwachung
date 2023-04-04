#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Hall Effect Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_hall_effect import BrickletHallEffect

# Callback function for edge count callback
def cb_edge_count(count, value):
    print("Count: " + str(count))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    he = BrickletHallEffect(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register edge count callback to function cb_edge_count
    he.register_callback(he.CALLBACK_EDGE_COUNT, cb_edge_count)

    # Set period for edge count callback to 0.05s (50ms)
    # Note: The edge count callback is only called every 0.05 seconds
    #       if the edge count has changed since the last call!
    he.set_edge_count_callback_period(50)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
