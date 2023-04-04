#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Temperature IR Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature_ir import BrickletTemperatureIR

# Callback function for object temperature callback
def cb_object_temperature(temperature):
    print("Object Temperature: " + str(temperature/10.0) + " °C")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    tir = BrickletTemperatureIR(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register object temperature callback to function cb_object_temperature
    tir.register_callback(tir.CALLBACK_OBJECT_TEMPERATURE, cb_object_temperature)

    # Set period for object temperature callback to 1s (1000ms)
    # Note: The object temperature callback is only called every second
    #       if the object temperature has changed since the last call!
    tir.set_object_temperature_callback_period(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
