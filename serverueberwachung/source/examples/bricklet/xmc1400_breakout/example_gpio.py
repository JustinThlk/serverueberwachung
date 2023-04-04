#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your XMC1400 Breakout Bricklet

import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_xmc1400_breakout import BrickletXMC1400Breakout

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    xb = BrickletXMC1400Breakout(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set Port 1, Pin 0 alternating high/low for 5 times with 1s delay
    for i in range(5):
        time.sleep(1)
        xb.set_gpio_config(1, 0, xb.GPIO_MODE_OUTPUT_PUSH_PULL, 0, False)
        time.sleep(1)
        xb.set_gpio_config(1, 0, xb.GPIO_MODE_OUTPUT_PUSH_PULL, 0, True)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
