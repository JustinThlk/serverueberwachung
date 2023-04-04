#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Rotary Encoder Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_encoder import BrickletRotaryEncoder

# Callback function for count callback
def cb_count(count):
    print("Count: " + str(count))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    re = BrickletRotaryEncoder(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register count callback to function cb_count
    re.register_callback(re.CALLBACK_COUNT, cb_count)

    # Set period for count callback to 0.05s (50ms)
    # Note: The count callback is only called every 0.05 seconds
    #       if the count has changed since the last call!
    re.set_count_callback_period(50)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
