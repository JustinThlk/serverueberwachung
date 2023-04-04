#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Counter Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_counter import BrickletIndustrialCounter

# Callback function for all counter callback
def cb_all_counter(counter):
    print("Counter (Channel 0): " + str(counter[0]))
    print("Counter (Channel 1): " + str(counter[1]))
    print("Counter (Channel 2): " + str(counter[2]))
    print("Counter (Channel 3): " + str(counter[3]))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ic = BrickletIndustrialCounter(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register all counter callback to function cb_all_counter
    ic.register_callback(ic.CALLBACK_ALL_COUNTER, cb_all_counter)

    # Set period for all counter callback to 1s (1000ms)
    ic.set_all_counter_callback_configuration(1000, True)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
