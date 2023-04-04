#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Joystick Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_joystick_v2 import BrickletJoystickV2

# Callback function for pressed callback
def cb_pressed(pressed):
    print("Pressed: " + str(pressed))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    j = BrickletJoystickV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register pressed callback to function cb_pressed
    j.register_callback(j.CALLBACK_PRESSED, cb_pressed)

    # Set period for pressed callback to 0.01s (10ms)
    j.set_pressed_callback_configuration(10, True)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
