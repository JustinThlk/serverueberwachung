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

    # Make 2 second beep with a frequency of 1kHz
    ps.set_beep(1000, 0, 2000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
