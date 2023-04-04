#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Segment Display 4x7 Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_segment_display_4x7_v2 import BrickletSegmentDisplay4x7V2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    sd = BrickletSegmentDisplay4x7V2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    sd.set_brightness(7) # Set to full brightness

    # Show "- 42" on the Display
    sd.set_numeric_value([-2, -1, 4, 2])

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
