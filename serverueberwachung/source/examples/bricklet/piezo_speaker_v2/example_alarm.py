#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Piezo Speaker Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_piezo_speaker_v2 import BrickletPiezoSpeakerV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ps = BrickletPiezoSpeakerV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # 10 seconds of loud annoying fast alarm
    ps.set_alarm(800, 2000, 10, 1, 10, 10000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
