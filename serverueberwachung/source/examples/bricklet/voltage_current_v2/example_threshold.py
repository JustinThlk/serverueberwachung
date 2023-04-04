#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Voltage/Current Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_voltage_current_v2 import BrickletVoltageCurrentV2

# Callback function for power callback
def cb_power(power):
    print("power: " + str(power/1000.0) + " W")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    vc = BrickletVoltageCurrentV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register power callback to function cb_power
    vc.register_callback(vc.CALLBACK_POWER, cb_power)

    # Configure threshold for power "greater than 10 W"
    # with a debounce period of 1s (1000ms)
    vc.set_power_callback_configuration(1000, False, ">", 10*1000, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
