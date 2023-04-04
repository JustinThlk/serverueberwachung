#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Temperature IR Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature_ir import BrickletTemperatureIR

# Callback function for object temperature reached callback
def cb_object_temperature_reached(temperature):
    print("Object Temperature: " + str(temperature/10.0) + " °C")
    print("The water is boiling!")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    tir = BrickletTemperatureIR(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set emissivity to 0.98 (emissivity of water, 65535 * 0.98 = 64224.299)
    tir.set_emissivity(64224)

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    tir.set_debounce_period(10000)

    # Register object temperature reached callback to function
    # cb_object_temperature_reached
    tir.register_callback(tir.CALLBACK_OBJECT_TEMPERATURE_REACHED,
                          cb_object_temperature_reached)

    # Configure threshold for object temperature "greater than 100 °C"
    tir.set_object_temperature_callback_threshold(">", 100*10, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
