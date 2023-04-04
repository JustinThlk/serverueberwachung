#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Humidity Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_humidity import BrickletHumidity

# Callback function for humidity reached callback
def cb_humidity_reached(humidity):
    print("Humidity: " + str(humidity/10.0) + " %RH")
    print("Recommended humidity for human comfort is 30 to 60 %RH.")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    h = BrickletHumidity(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    h.set_debounce_period(10000)

    # Register humidity reached callback to function cb_humidity_reached
    h.register_callback(h.CALLBACK_HUMIDITY_REACHED, cb_humidity_reached)

    # Configure threshold for humidity "outside of 30 to 60 %RH"
    h.set_humidity_callback_threshold("o", 30*10, 60*10)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
