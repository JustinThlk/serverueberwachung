#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Ambient Light Bricklet 3.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ambient_light_v3 import BrickletAmbientLightV3

# Callback function for illuminance callback
def cb_illuminance(illuminance):
    print("Illuminance: " + str(illuminance/100.0) + " lx")
    print("Too bright, close the curtains!")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    al = BrickletAmbientLightV3(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register illuminance callback to function cb_illuminance
    al.register_callback(al.CALLBACK_ILLUMINANCE, cb_illuminance)

    # Configure threshold for illuminance "greater than 500 lx"
    # with a debounce period of 1s (1000ms)
    al.set_illuminance_callback_configuration(1000, False, ">", 500*100, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
