#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Sound Intensity Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_sound_intensity import BrickletSoundIntensity

# Callback function for intensity reached callback
def cb_intensity_reached(intensity):
    print("Intensity: " + str(intensity))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    si = BrickletSoundIntensity(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 1 second (1000ms)
    si.set_debounce_period(1000)

    # Register intensity reached callback to function cb_intensity_reached
    si.register_callback(si.CALLBACK_INTENSITY_REACHED, cb_intensity_reached)

    # Configure threshold for intensity "greater than 2000"
    si.set_intensity_callback_threshold(">", 2000, 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
