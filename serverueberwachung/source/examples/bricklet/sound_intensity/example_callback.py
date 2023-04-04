#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Sound Intensity Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_sound_intensity import BrickletSoundIntensity

# Callback function for intensity callback
def cb_intensity(intensity):
    print("Intensity: " + str(intensity))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    si = BrickletSoundIntensity(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register intensity callback to function cb_intensity
    si.register_callback(si.CALLBACK_INTENSITY, cb_intensity)

    # Set period for intensity callback to 0.05s (50ms)
    # Note: The intensity callback is only called every 0.05 seconds
    #       if the intensity has changed since the last call!
    si.set_intensity_callback_period(50)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
