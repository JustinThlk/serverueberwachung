#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your CO2 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_co2 import BrickletCO2

# Callback function for CO2 concentration reached callback
def cb_co2_concentration_reached(co2_concentration):
    print("CO2 Concentration: " + str(co2_concentration) + " ppm")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    co2 = BrickletCO2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    co2.set_debounce_period(10000)

    # Register CO2 concentration reached callback to function cb_co2_concentration_reached
    co2.register_callback(co2.CALLBACK_CO2_CONCENTRATION_REACHED,
                          cb_co2_concentration_reached)

    # Configure threshold for CO2 concentration "greater than 750 ppm"
    co2.set_co2_concentration_callback_threshold(">", 750, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
