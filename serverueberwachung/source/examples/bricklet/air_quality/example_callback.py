#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Air Quality Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_air_quality import BrickletAirQuality

# Callback function for all values callback
def cb_all_values(iaq_index, iaq_index_accuracy, temperature, humidity, air_pressure):
    print("IAQ Index: " + str(iaq_index))

    if iaq_index_accuracy == BrickletAirQuality.ACCURACY_UNRELIABLE:
        print("IAQ Index Accuracy: Unreliable")
    elif iaq_index_accuracy == BrickletAirQuality.ACCURACY_LOW:
        print("IAQ Index Accuracy: Low")
    elif iaq_index_accuracy == BrickletAirQuality.ACCURACY_MEDIUM:
        print("IAQ Index Accuracy: Medium")
    elif iaq_index_accuracy == BrickletAirQuality.ACCURACY_HIGH:
        print("IAQ Index Accuracy: High")

    print("Temperature: " + str(temperature/100.0) + " °C")
    print("Humidity: " + str(humidity/100.0) + " %RH")
    print("Air Pressure: " + str(air_pressure/100.0) + " hPa")
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    aq = BrickletAirQuality(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register all values callback to function cb_all_values
    aq.register_callback(aq.CALLBACK_ALL_VALUES, cb_all_values)

    # Set period for all values callback to 1s (1000ms)
    aq.set_all_values_callback_configuration(1000, False)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
