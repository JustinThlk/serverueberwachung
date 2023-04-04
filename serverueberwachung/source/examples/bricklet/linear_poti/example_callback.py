#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Linear Poti Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_linear_poti import BrickletLinearPoti

# Callback function for position callback
def cb_position(position):
    print("Position: " + str(position) + " %") # Range: 0 to 100

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lp = BrickletLinearPoti(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register position callback to function cb_position
    lp.register_callback(lp.CALLBACK_POSITION, cb_position)

    # Set period for position callback to 0.05s (50ms)
    # Note: The position callback is only called every 0.05 seconds
    #       if the position has changed since the last call!
    lp.set_position_callback_period(50)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
