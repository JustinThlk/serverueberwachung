#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Sound Intensity Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_sound_intensity import BrickletSoundIntensity

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    si = BrickletSoundIntensity(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current intensity
    intensity = si.get_intensity()
    print("Intensity: " + str(intensity))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
