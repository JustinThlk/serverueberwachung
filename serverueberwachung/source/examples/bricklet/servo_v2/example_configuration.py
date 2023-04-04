#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Servo Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_servo_v2 import BrickletServoV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    s = BrickletServoV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Servo 1: Connected to port 0, period of 19.5ms, pulse width of 1 to 2ms
    #          and operating angle -100 to 100°
    s.set_degree(0, -10000, 10000)
    s.set_pulse_width(0, 1000, 2000)
    s.set_period(0, 19500)
    s.set_motion_configuration(0, 500000, 1000,
                               1000) # Full velocity with slow ac-/deceleration


    # Servo 2: Connected to port 5, period of 20ms, pulse width of 0.95 to 1.95ms
    #          and operating angle -90 to 90°
    s.set_degree(5, -9000, 9000)
    s.set_pulse_width(5, 950, 1950)
    s.set_period(5, 20000)
    s.set_motion_configuration(5, 500000, 500000,
                               500000) # Full velocity with full ac-/deceleration

    s.set_position(0, 10000) # Set to most right position
    s.set_enable(0, True)

    s.set_position(5, -9000) # Set to most left position
    s.set_enable(5, True)

    input("Press key to exit\n") # Use raw_input() in Python 2

    s.set_enable(0, False)
    s.set_enable(5, False)

    ipcon.disconnect()
