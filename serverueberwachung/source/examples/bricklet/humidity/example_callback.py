#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Humidity Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_humidity import BrickletHumidity

# Callback function for humidity callback
def cb_humidity(humidity):
    print("Humidity: " + str(humidity/10.0) + " %RH")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    h = BrickletHumidity(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register humidity callback to function cb_humidity
    h.register_callback(h.CALLBACK_HUMIDITY, cb_humidity)

    # Set period for humidity callback to 1s (1000ms)
    # Note: The humidity callback is only called every second
    #       if the humidity has changed since the last call!
    h.set_humidity_callback_period(1000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
