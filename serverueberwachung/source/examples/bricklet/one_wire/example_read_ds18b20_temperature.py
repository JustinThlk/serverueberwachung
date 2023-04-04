#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your One Wire Bricklet

import time

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_one_wire import BrickletOneWire

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ow = BrickletOneWire(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    ow.write_command(0, 78) # WRITE SCRATCHPAD
    ow.write(0) # ALARM H (unused)
    ow.write(0) # ALARM L (unused)
    ow.write(127) # CONFIGURATION: 12-bit mode

    # Read temperature 10 times
    for i in range(10):
        ow.write_command(0, 68) # CONVERT T (start temperature conversion)
        time.sleep(1) # Wait for conversion to finish
        ow.write_command(0, 190) # READ SCRATCHPAD

        t_low = ow.read().data
        t_high = ow.read().data

        temperature = t_low | (t_high << 8)

        # Negative 12-bit values are sign-extended to 16-bit two's complement
        if temperature > 1 << 12:
            temperature -= 1 << 16

        # 12-bit mode measures in units of 1/16°C
        print("Temperature: " + str(temperature/16.0) + " °C")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
