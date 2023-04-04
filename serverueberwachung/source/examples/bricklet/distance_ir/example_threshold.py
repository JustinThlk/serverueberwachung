#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Distance IR Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir import BrickletDistanceIR

# Callback function for distance reached callback
def cb_distance_reached(distance):
    print("Distance: " + str(distance/10.0) + " cm")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    dir = BrickletDistanceIR(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    dir.set_debounce_period(10000)

    # Register distance reached callback to function cb_distance_reached
    dir.register_callback(dir.CALLBACK_DISTANCE_REACHED, cb_distance_reached)

    # Configure threshold for distance "smaller than 30 cm"
    dir.set_distance_callback_threshold("<", 30*10, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
