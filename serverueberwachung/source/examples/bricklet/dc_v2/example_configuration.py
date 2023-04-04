#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your DC Bricklet 2.0

import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_dc_v2 import BrickletDCV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    dc = BrickletDCV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    dc.set_drive_mode(dc.DRIVE_MODE_DRIVE_COAST)
    dc.set_pwm_frequency(10000) # Use PWM frequency of 10 kHz
    dc.set_motion(4096,
                  16384) # Slow acceleration (12.5 %/s), fast decceleration (50 %/s) for stopping
    dc.set_velocity(32767) # Full speed forward (100 %)
    dc.set_enabled(True) # Enable motor power

    input("Press key to exit\n") # Use raw_input() in Python 2

    dc.set_velocity(0) # Stop motor before disabling motor power
    time.sleep(2) # Wait for motor to actually stop: velocity (100 %) / decceleration (50 %/s) = 2 s
    dc.set_enabled(False) # Disable motor power

    ipcon.disconnect()
