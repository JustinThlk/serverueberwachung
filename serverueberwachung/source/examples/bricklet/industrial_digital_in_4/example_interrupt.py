#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Digital In 4 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_digital_in_4 import BrickletIndustrialDigitalIn4

# Callback function for interrupt callback
def cb_interrupt(interrupt_mask, value_mask):
    print("Interrupt Mask: " + format(interrupt_mask, "04b"))
    print("Value Mask: " + format(value_mask, "04b"))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    idi4 = BrickletIndustrialDigitalIn4(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register interrupt callback to function cb_interrupt
    idi4.register_callback(idi4.CALLBACK_INTERRUPT, cb_interrupt)

    # Enable interrupt on pin 0
    idi4.set_interrupt(1 << 0)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
