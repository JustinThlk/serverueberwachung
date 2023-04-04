#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XXYYZZ" # Change XXYYZZ to the UID of your HAT Zero Brick

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_hat_zero import BrickHATZero

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    hz = BrickHATZero(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current voltage
    voltage = hz.get_usb_voltage()
    print("Voltage: " + str(voltage/1000.0) + " V")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
