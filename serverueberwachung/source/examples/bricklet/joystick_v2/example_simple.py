#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Joystick Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_joystick_v2 import BrickletJoystickV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    j = BrickletJoystickV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current position
    x, y = j.get_position()

    print("Position [X]: " + str(x))
    print("Position [Y]: " + str(y))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
