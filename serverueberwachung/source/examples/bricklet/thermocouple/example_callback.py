#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Thermocouple Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_thermocouple import BrickletThermocouple

# Callback function for temperature callback
def cb_temperature(temperature):
    print("Temperature: " + str(temperature/100.0) + " °C")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    t = BrickletThermocouple(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register temperature callback to function cb_temperature
    t.register_callback(t.CALLBACK_TEMPERATURE, cb_temperature)

    # Set period for temperature callback to 1s (1000ms)
    # Note: The temperature callback is only called every second
    #       if the temperature has changed since the last call!
    t.set_temperature_callback_period(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
