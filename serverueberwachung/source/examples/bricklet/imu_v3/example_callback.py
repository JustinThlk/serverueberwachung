#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your IMU Bricklet 3.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_imu_v3 import BrickletIMUV3

# Callback function for quaternion callback
def cb_quaternion(w, x, y, z):
    print("Quaternion [W]: " + str(w/16383.0))
    print("Quaternion [X]: " + str(x/16383.0))
    print("Quaternion [Y]: " + str(y/16383.0))
    print("Quaternion [Z]: " + str(z/16383.0))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    imu = BrickletIMUV3(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register quaternion callback to function cb_quaternion
    imu.register_callback(imu.CALLBACK_QUATERNION, cb_quaternion)

    # Set period for quaternion callback to 0.1s (100ms)
    imu.set_quaternion_callback_configuration(100, False)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
