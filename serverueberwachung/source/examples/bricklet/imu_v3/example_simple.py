#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your IMU Bricklet 3.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_imu_v3 import BrickletIMUV3

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    imu = BrickletIMUV3(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current quaternion
    w, x, y, z = imu.get_quaternion()

    print("Quaternion [W]: " + str(w/16383.0))
    print("Quaternion [X]: " + str(x/16383.0))
    print("Quaternion [Y]: " + str(y/16383.0))
    print("Quaternion [Z]: " + str(z/16383.0))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
