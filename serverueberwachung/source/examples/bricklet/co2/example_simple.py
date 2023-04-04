#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your CO2 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_co2 import BrickletCO2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    co2 = BrickletCO2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current CO2 concentration
    co2_concentration = co2.get_co2_concentration()
    print("CO2 Concentration: " + str(co2_concentration) + " ppm")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
