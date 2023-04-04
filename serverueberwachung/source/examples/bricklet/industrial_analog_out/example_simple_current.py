#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Analog Out Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_analog_out import BrickletIndustrialAnalogOut

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    iao = BrickletIndustrialAnalogOut(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set output current to 4.5mA
    iao.set_current(4500)
    iao.enable()

    input("Press key to exit\n") # Use raw_input() in Python 2

    iao.disable()

    ipcon.disconnect()
