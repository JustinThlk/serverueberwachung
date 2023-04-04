#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Dual 0-20mA Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_dual_0_20ma import BrickletIndustrialDual020mA

# Callback function for current reached callback
def cb_current_reached(sensor, current):
    print("Sensor: " + str(sensor))
    print("Current: " + str(current/1000000.0) + " mA")
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    id020 = BrickletIndustrialDual020mA(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    id020.set_debounce_period(10000)

    # Register current reached callback to function cb_current_reached
    id020.register_callback(id020.CALLBACK_CURRENT_REACHED, cb_current_reached)

    # Configure threshold for current (sensor 1) "greater than 10 mA"
    id020.set_current_callback_threshold(1, ">", 10*1000000, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
