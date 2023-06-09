#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "172.20.10.57"
PORT = 4223
UID = "ML4" # Change XYZ to the UID of your Motion Detector Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_motion_detector_v2 import BrickletMotionDetectorV2

# Callback function for motion detected callback
def cb_motion_detected():
    print("Motion Detected")

# Callback function for detection cycle ended callback
def cb_detection_cycle_ended():
    print("Detection Cycle Ended (next detection possible in ~2 seconds)")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    md = BrickletMotionDetectorV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register motion detected callback to function cb_motion_detected
    md.register_callback(md.CALLBACK_MOTION_DETECTED, cb_motion_detected)

    # Register detection cycle ended callback to function cb_detection_cycle_ended
    md.register_callback(md.CALLBACK_DETECTION_CYCLE_ENDED, cb_detection_cycle_ended)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
