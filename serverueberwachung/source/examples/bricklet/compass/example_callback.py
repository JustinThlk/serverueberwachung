#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Compass Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_compass import BrickletCompass

# Callback function for heading callback
def cb_heading(heading):
    print("Heading: " + str(heading/10.0) + " °")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    c = BrickletCompass(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register heading callback to function cb_heading
    c.register_callback(c.CALLBACK_HEADING, cb_heading)

    # Set period for heading callback to 0.1s (100ms) without a threshold
    c.set_heading_callback_configuration(100, False, "x", 0, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
