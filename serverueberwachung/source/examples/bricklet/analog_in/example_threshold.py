#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Analog In Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_analog_in import BrickletAnalogIn

# Callback function for voltage reached callback
def cb_voltage_reached(voltage):
    print("Voltage: " + str(voltage/1000.0) + " V")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ai = BrickletAnalogIn(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    ai.set_debounce_period(10000)

    # Register voltage reached callback to function cb_voltage_reached
    ai.register_callback(ai.CALLBACK_VOLTAGE_REACHED, cb_voltage_reached)

    # Configure threshold for voltage "smaller than 5 V"
    ai.set_voltage_callback_threshold("<", 5*1000, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
