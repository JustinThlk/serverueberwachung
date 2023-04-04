#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use ambient air pressure from Air Quality Bricklet to
# for air pressure compensation feature of CO2 Bricklet 2.0.

HOST = "localhost"
PORT = 4223
UID_CO2 = "XYZ1" # Change XYZ1 to the UID of your CO2 Bricklet 2.0
UID_AQ  = "XYZ2" # Change XYZ2 to the UID of your Air Quality Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_co2_v2 import BrickletCO2V2
from tinkerforge.bricklet_air_quality import BrickletAirQuality

import time

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    co2 = BrickletCO2V2(UID_CO2, ipcon) # Create device object
    aq = BrickletAirQuality(UID_AQ, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get air pressure in 0.01 hPa
    air_pressure = aq.get_air_pressure()

    # Set air pressure for calibration in hPa
    co2.set_air_pressure(air_pressure // 100)

    # Get current all values
    while True:
        co2_concentration, temperature, humidity = co2.get_all_values()

        print("CO2 Concentration: " + str(co2_concentration) + " ppm")
        print("Temperature: " + str(temperature/100.0) + " °C")
        print("Humidity: " + str(humidity/100.0) + " %RH")
        print("")

        time.sleep(1)
