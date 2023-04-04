#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Dual Analog In Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_dual_analog_in import BrickletIndustrialDualAnalogIn

# Callback function for voltage callback
def cb_voltage(channel, voltage):
    print("Channel: " + str(channel))
    print("Voltage: " + str(voltage/1000.0) + " V")
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    idai = BrickletIndustrialDualAnalogIn(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register voltage callback to function cb_voltage
    idai.register_callback(idai.CALLBACK_VOLTAGE, cb_voltage)

    # Set period for voltage (channel 1) callback to 1s (1000ms)
    # Note: The voltage (channel 1) callback is only called every second
    #       if the voltage (channel 1) has changed since the last call!
    idai.set_voltage_callback_period(1, 1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
