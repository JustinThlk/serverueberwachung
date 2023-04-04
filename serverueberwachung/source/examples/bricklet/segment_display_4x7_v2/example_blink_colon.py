#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Segment Display 4x7 Bricklet 2.0

import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_segment_display_4x7_v2 import BrickletSegmentDisplay4x7V2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    sd = BrickletSegmentDisplay4x7V2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    sd.set_brightness(7) # Set to full brightness

    # Blink colon 10 times
    for i in range(10):

        # Activate segments of colon
        sd.set_selected_segment(32, True)
        sd.set_selected_segment(33, True)

        time.sleep(0.25)

        # Deactivate segments of colon
        sd.set_selected_segment(32, False)
        sd.set_selected_segment(33, False)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
