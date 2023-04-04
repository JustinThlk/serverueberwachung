#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Air Quality Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_air_quality import BrickletAirQuality

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    aq = BrickletAirQuality(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current all values
    iaq_index, iaq_index_accuracy, temperature, humidity, \
      air_pressure = aq.get_all_values()

    print("IAQ Index: " + str(iaq_index))

    if iaq_index_accuracy == aq.ACCURACY_UNRELIABLE:
        print("IAQ Index Accuracy: Unreliable")
    elif iaq_index_accuracy == aq.ACCURACY_LOW:
        print("IAQ Index Accuracy: Low")
    elif iaq_index_accuracy == aq.ACCURACY_MEDIUM:
        print("IAQ Index Accuracy: Medium")
    elif iaq_index_accuracy == aq.ACCURACY_HIGH:
        print("IAQ Index Accuracy: High")

    print("Temperature: " + str(temperature/100.0) + " °C")
    print("Humidity: " + str(humidity/100.0) + " %RH")
    print("Air Pressure: " + str(air_pressure/100.0) + " hPa")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
