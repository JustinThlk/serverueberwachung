#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Rotary Encoder Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_encoder_v2 import BrickletRotaryEncoderV2

# Callback function for count callback
def cb_count(count):
    print("Count: " + str(count))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    re = BrickletRotaryEncoderV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register count callback to function cb_count
    re.register_callback(re.CALLBACK_COUNT, cb_count)

    # Set period for count callback to 1s (1000ms) without a threshold
    re.set_count_callback_configuration(1000, False, "x", 0, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
