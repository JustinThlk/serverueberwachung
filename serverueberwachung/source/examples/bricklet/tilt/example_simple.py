#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Tilt Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_tilt import BrickletTilt

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    t = BrickletTilt(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current tilt state
    state = t.get_tilt_state()

    if state == t.TILT_STATE_CLOSED:
        print("Tilt State: Closed")
    elif state == t.TILT_STATE_OPEN:
        print("Tilt State: Open")
    elif state == t.TILT_STATE_CLOSED_VIBRATING:
        print("Tilt State: Closed Vibrating")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
