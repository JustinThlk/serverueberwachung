#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Dual 0-20mA Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_dual_0_20ma import BrickletIndustrialDual020mA

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    id020 = BrickletIndustrialDual020mA(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current current from sensor 1
    current = id020.get_current(1)
    print("Current (Sensor 1): " + str(current/1000000.0) + " mA")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
