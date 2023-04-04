#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Isolator Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_isolator import BrickletIsolator

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    i = BrickletIsolator(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current statistics
    messages_from_brick, messages_from_bricklet, connected_bricklet_device_identifier, \
      connected_bricklet_uid = i.get_statistics()

    print("Messages From Brick: " + str(messages_from_brick))
    print("Messages From Bricklet: " + str(messages_from_bricklet))
    print("Connected Bricklet Device Identifier: " + str(connected_bricklet_device_identifier))
    print("Connected Bricklet UID: " + connected_bricklet_uid)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
