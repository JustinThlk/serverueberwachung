#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Multi Touch Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_multi_touch_v2 import BrickletMultiTouchV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    mt = BrickletMultiTouchV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current touch state
    state = mt.get_touch_state()

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

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
