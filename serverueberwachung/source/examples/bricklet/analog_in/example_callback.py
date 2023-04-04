#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Analog In Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_analog_in import BrickletAnalogIn

# Callback function for voltage callback
def cb_voltage(voltage):
    print("Voltage: " + str(voltage/1000.0) + " V")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ai = BrickletAnalogIn(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register voltage callback to function cb_voltage
    ai.register_callback(ai.CALLBACK_VOLTAGE, cb_voltage)

    # Set period for voltage callback to 1s (1000ms)
    # Note: The voltage callback is only called every second
    #       if the voltage has changed since the last call!
    ai.set_voltage_callback_period(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
