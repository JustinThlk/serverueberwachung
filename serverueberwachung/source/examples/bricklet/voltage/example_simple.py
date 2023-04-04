#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Voltage Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_voltage import BrickletVoltage

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    v = BrickletVoltage(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current voltage
    voltage = v.get_voltage()
    print("Voltage: " + str(voltage/1000.0) + " V")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
