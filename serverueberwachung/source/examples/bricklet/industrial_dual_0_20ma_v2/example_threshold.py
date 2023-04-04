#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Dual 0-20mA Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_dual_0_20ma_v2 import BrickletIndustrialDual020mAV2

# Callback function for current callback
def cb_current(channel, current):
    print("Channel: " + str(channel))
    print("Current: " + str(current/1000000.0) + " mA")
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    id020 = BrickletIndustrialDual020mAV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register current callback to function cb_current
    id020.register_callback(id020.CALLBACK_CURRENT, cb_current)

    # Configure threshold for current (channel 0) "greater than 10 mA"
    # with a debounce period of 10s (10000ms)
    id020.set_current_callback_configuration(0, 10000, False, ">", 10*1000000, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
