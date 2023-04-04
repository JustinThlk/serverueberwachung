#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Servo Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_servo_v2 import BrickletServoV2

# Use position reached callback to swing back and forth
def cb_position_reached(servo_channel, position):
    if position == 9000:
        print('Position: 90°, going to -90°')
        s.set_position(servo_channel, -9000)
    elif position == -9000:
        print('Position: -90°, going to 90°')
        s.set_position(servo_channel, 9000)
    else:
        print('Error') # Can only happen if another program sets position

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    s = BrickletServoV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register position reached callback to function cb_position_reached
    s.register_callback(s.CALLBACK_POSITION_REACHED, cb_position_reached)

    # Enable position reached callback
    s.set_position_reached_callback_configuration(0, True)

    # Set velocity to 100°/s. This has to be smaller or equal to the
    # maximum velocity of the servo you are using, otherwise the position
    # reached callback will be called too early
    s.set_motion_configuration(0, 10000, 500000, 500000)
    s.set_position(0, 9000)
    s.set_enable(0, True)

    input("Press key to exit\n") # Use raw_input() in Python 2

    s.set_enable(0, False)

    ipcon.disconnect()
