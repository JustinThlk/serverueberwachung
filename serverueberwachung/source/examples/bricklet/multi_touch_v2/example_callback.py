#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Multi Touch Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_multi_touch_v2 import BrickletMultiTouchV2

# Callback function for touch state callback
def cb_touch_state(state):
    print("Electrode 0: " + str(state[0]))
    print("Electrode 1: " + str(state[1]))
    print("Electrode 2: " + str(state[2]))
    print("Electrode 3: " + str(state[3]))
    print("Electrode 4: " + str(state[4]))
    print("Electrode 5: " + str(state[5]))
    print("Electrode 6: " + str(state[6]))
    print("Electrode 7: " + str(state[7]))
    print("Electrode 8: " + str(state[8]))
    print("Electrode 9: " + str(state[9]))
    print("Electrode 10: " + str(state[10]))
    print("Electrode 11: " + str(state[11]))
    print("Proximity: " + str(state[12]))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    mt = BrickletMultiTouchV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register touch state callback to function cb_touch_state
    mt.register_callback(mt.CALLBACK_TOUCH_STATE, cb_touch_state)

    # Set period for touch state callback to 0.01s (10ms)
    mt.set_touch_state_callback_configuration(10, True)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
