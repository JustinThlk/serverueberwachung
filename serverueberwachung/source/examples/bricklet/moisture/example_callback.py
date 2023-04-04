#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Moisture Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_moisture import BrickletMoisture

# Callback function for moisture value callback
def cb_moisture(moisture):
    print("Moisture Value: " + str(moisture))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    m = BrickletMoisture(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register moisture value callback to function cb_moisture
    m.register_callback(m.CALLBACK_MOISTURE, cb_moisture)

    # Set period for moisture value callback to 1s (1000ms)
    # Note: The moisture value callback is only called every second
    #       if the moisture value has changed since the last call!
    m.set_moisture_callback_period(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
