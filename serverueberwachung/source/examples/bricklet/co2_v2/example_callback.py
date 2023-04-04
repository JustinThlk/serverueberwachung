#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your CO2 Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_co2_v2 import BrickletCO2V2

# Callback function for all values callback
def cb_all_values(co2_concentration, temperature, humidity):
    print("CO2 Concentration: " + str(co2_concentration) + " ppm")
    print("Temperature: " + str(temperature/100.0) + " °C")
    print("Humidity: " + str(humidity/100.0) + " %RH")
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    co2 = BrickletCO2V2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register all values callback to function cb_all_values
    co2.register_callback(co2.CALLBACK_ALL_VALUES, cb_all_values)

    # Set period for all values callback to 1s (1000ms)
    co2.set_all_values_callback_configuration(1000, False)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
