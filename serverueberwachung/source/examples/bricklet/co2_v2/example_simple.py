#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your CO2 Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_co2_v2 import BrickletCO2V2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    co2 = BrickletCO2V2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current all values
    co2_concentration, temperature, humidity = co2.get_all_values()

    print("CO2 Concentration: " + str(co2_concentration) + " ppm")
    print("Temperature: " + str(temperature/100.0) + " °C")
    print("Humidity: " + str(humidity/100.0) + " %RH")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
