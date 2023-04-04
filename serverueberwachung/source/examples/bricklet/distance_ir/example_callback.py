#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Distance IR Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir import BrickletDistanceIR

# Callback function for distance callback
def cb_distance(distance):
    print("Distance: " + str(distance/10.0) + " cm")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    dir = BrickletDistanceIR(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register distance callback to function cb_distance
    dir.register_callback(dir.CALLBACK_DISTANCE, cb_distance)

    # Set period for distance callback to 0.2s (200ms)
    # Note: The distance callback is only called every 0.2 seconds
    #       if the distance has changed since the last call!
    dir.set_distance_callback_period(200)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
