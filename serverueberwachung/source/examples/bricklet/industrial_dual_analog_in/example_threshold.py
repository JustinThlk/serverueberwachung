#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Dual Analog In Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_dual_analog_in import BrickletIndustrialDualAnalogIn

# Callback function for voltage reached callback
def cb_voltage_reached(channel, voltage):
    print("Channel: " + str(channel))
    print("Voltage: " + str(voltage/1000.0) + " V")
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    idai = BrickletIndustrialDualAnalogIn(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    idai.set_debounce_period(10000)

    # Register voltage reached callback to function cb_voltage_reached
    idai.register_callback(idai.CALLBACK_VOLTAGE_REACHED, cb_voltage_reached)

    # Configure threshold for voltage (channel 1) "greater than 10 V"
    idai.set_voltage_callback_threshold(1, ">", 10*1000, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
