#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Dual 0-20mA Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_dual_0_20ma import BrickletIndustrialDual020mA

# Callback function for current callback
def cb_current(sensor, current):
    print("Sensor: " + str(sensor))
    print("Current: " + str(current/1000000.0) + " mA")
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    id020 = BrickletIndustrialDual020mA(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register current callback to function cb_current
    id020.register_callback(id020.CALLBACK_CURRENT, cb_current)

    # Set period for current (sensor 1) callback to 1s (1000ms)
    # Note: The current (sensor 1) callback is only called every second
    #       if the current (sensor 1) has changed since the last call!
    id020.set_current_callback_period(1, 1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
