#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Remote Switch Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_remote_switch_v2 import BrickletRemoteSwitchV2

# Callback function for remote status a callback
def cb_remote_status_a(house_code, receiver_code, switch_to, repeats):
    print("House Code: " + str(house_code))
    print("Receiver Code: " + str(receiver_code))

    if switch_to == BrickletRemoteSwitchV2.SWITCH_TO_OFF:
        print("Switch To: Off")
    elif switch_to == BrickletRemoteSwitchV2.SWITCH_TO_ON:
        print("Switch To: On")

    print("Repeats: " + str(repeats))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rs = BrickletRemoteSwitchV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Configure to receive from remote type A with minimum repeats set to 1 and enable callback
    rs.set_remote_configuration(rs.REMOTE_TYPE_A, 1, True)

    # Register remote status a callback to function cb_remote_status_a
    rs.register_callback(rs.CALLBACK_REMOTE_STATUS_A, cb_remote_status_a)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
