#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your CO2 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_co2 import BrickletCO2

# Callback function for CO2 concentration callback
def cb_co2_concentration(co2_concentration):
    print("CO2 Concentration: " + str(co2_concentration) + " ppm")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    co2 = BrickletCO2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register CO2 concentration callback to function cb_co2_concentration
    co2.register_callback(co2.CALLBACK_CO2_CONCENTRATION, cb_co2_concentration)

    # Set period for CO2 concentration callback to 1s (1000ms)
    # Note: The CO2 concentration callback is only called every second
    #       if the CO2 concentration has changed since the last call!
    co2.set_co2_concentration_callback_period(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
