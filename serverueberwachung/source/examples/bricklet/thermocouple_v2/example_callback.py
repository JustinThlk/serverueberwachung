#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Thermocouple Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_thermocouple_v2 import BrickletThermocoupleV2

# Callback function for temperature callback
def cb_temperature(temperature):
    print("Temperature: " + str(temperature/100.0) + " °C")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    t = BrickletThermocoupleV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register temperature callback to function cb_temperature
    t.register_callback(t.CALLBACK_TEMPERATURE, cb_temperature)

    # Set period for temperature callback to 1s (1000ms) without a threshold
    t.set_temperature_callback_configuration(1000, False, "x", 0, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
