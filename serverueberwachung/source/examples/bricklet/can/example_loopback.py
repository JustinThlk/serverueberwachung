#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your CAN Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_can import BrickletCAN

# Callback function for frame read callback
def cb_frame_read(frame_type, identifier, data, length):
    if frame_type == BrickletCAN.FRAME_TYPE_STANDARD_DATA:
        print("Frame Type: Standard Data")
    elif frame_type == BrickletCAN.FRAME_TYPE_STANDARD_REMOTE:
        print("Frame Type: Standard Remote")
    elif frame_type == BrickletCAN.FRAME_TYPE_EXTENDED_DATA:
        print("Frame Type: Extended Data")
    elif frame_type == BrickletCAN.FRAME_TYPE_EXTENDED_REMOTE:
        print("Frame Type: Extended Remote")

    print("Identifier: " + str(identifier))
    print("Data (Length: " + str(length) + "): " + ", ".join(map(str, data[:min(length, 8)])))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    can = BrickletCAN(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Configure transceiver for loopback mode
    can.set_configuration(can.BAUD_RATE_1000KBPS, can.TRANSCEIVER_MODE_LOOPBACK, 0)

    # Register frame read callback to function cb_frame_read
    can.register_callback(can.CALLBACK_FRAME_READ, cb_frame_read)

    # Enable frame read callback
    can.enable_frame_read_callback()

    # Write standard data frame with identifier 1742 and 3 bytes of data
    can.write_frame(can.FRAME_TYPE_STANDARD_DATA, 1742, [42, 23, 17, 0, 0, 0, 0, 0], 3)

    input("Press key to exit\n") # Use raw_input() in Python 2

    can.disable_frame_read_callback()

    ipcon.disconnect()
