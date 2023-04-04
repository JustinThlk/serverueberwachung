#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Moisture Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_moisture import BrickletMoisture

# Callback function for moisture value reached callback
def cb_moisture_reached(moisture):
    print("Moisture Value: " + str(moisture))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    m = BrickletMoisture(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 1 second (1000ms)
    m.set_debounce_period(1000)

    # Register moisture value reached callback to function cb_moisture_reached
    m.register_callback(m.CALLBACK_MOISTURE_REACHED, cb_moisture_reached)

    # Configure threshold for moisture value "greater than 200"
    m.set_moisture_callback_threshold(">", 200, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
