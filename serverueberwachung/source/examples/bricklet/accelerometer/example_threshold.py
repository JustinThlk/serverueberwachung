#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Accelerometer Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_accelerometer import BrickletAccelerometer

# Callback function for acceleration reached callback
def cb_acceleration_reached(x, y, z):
    print("Acceleration [X]: " + str(x/1000.0) + " g")
    print("Acceleration [Y]: " + str(y/1000.0) + " g")
    print("Acceleration [Z]: " + str(z/1000.0) + " g")
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    a = BrickletAccelerometer(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    a.set_debounce_period(10000)

    # Register acceleration reached callback to function cb_acceleration_reached
    a.register_callback(a.CALLBACK_ACCELERATION_REACHED, cb_acceleration_reached)

    # Configure threshold for acceleration "greater than 2 g, 2 g, 2 g"
    a.set_acceleration_callback_threshold(">", 2*1000, 0, 2*1000, 0, 2*1000, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
