#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Laser Range Finder Bricklet 2.0

import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_laser_range_finder_v2 import BrickletLaserRangeFinderV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lrf = BrickletLaserRangeFinderV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Turn laser on and wait 250ms for very first measurement to be ready
    lrf.set_enable(True)
    time.sleep(0.25)

    # Get current distance
    distance = lrf.get_distance()
    print("Distance: " + str(distance) + " cm")

    input("Press key to exit\n") # Use raw_input() in Python 2

    # Turn laser off
    lrf.set_enable(False)

    ipcon.disconnect()
