#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Distance IR Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir_v2 import BrickletDistanceIRV2

# Callback function for distance callback
def cb_distance(distance):
    print("Distance: " + str(distance/10.0) + " cm")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    dir = BrickletDistanceIRV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register distance callback to function cb_distance
    dir.register_callback(dir.CALLBACK_DISTANCE, cb_distance)

    # Configure threshold for distance "smaller than 30 cm"
    # with a debounce period of 1s (1000ms)
    dir.set_distance_callback_configuration(1000, False, "<", 30*10, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
