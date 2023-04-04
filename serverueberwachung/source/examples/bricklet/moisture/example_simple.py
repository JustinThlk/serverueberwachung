#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Moisture Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_moisture import BrickletMoisture

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    m = BrickletMoisture(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current moisture value
    moisture = m.get_moisture_value()
    print("Moisture Value: " + str(moisture))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
