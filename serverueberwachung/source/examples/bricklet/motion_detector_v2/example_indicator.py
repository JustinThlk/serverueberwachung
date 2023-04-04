#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Motion Detector Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_motion_detector_v2 import BrickletMotionDetectorV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    md = BrickletMotionDetectorV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Turn blue backlight LEDs on (maximum brightness)
    md.set_indicator(255, 255, 255)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
