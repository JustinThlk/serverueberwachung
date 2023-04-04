#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Laser Range Finder Bricklet 2.0

import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_laser_range_finder_v2 import BrickletLaserRangeFinderV2

# Callback function for distance callback
def cb_distance(distance):
    print("Distance: " + str(distance) + " cm")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lrf = BrickletLaserRangeFinderV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Turn laser on and wait 250ms for very first measurement to be ready
    lrf.set_enable(True)
    time.sleep(0.25)

    # Register distance callback to function cb_distance
    lrf.register_callback(lrf.CALLBACK_DISTANCE, cb_distance)

    # Configure threshold for distance "greater than 20 cm"
    # with a debounce period of 1s (1000ms)
    lrf.set_distance_callback_configuration(1000, False, ">", 20, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2

    # Turn laser off
    lrf.set_enable(False)

    ipcon.disconnect()
