#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your IO-16 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_io16 import BrickletIO16

# Callback function for interrupt callback
def cb_interrupt(port, interrupt_mask, value_mask):
    print("Port: " + port)
    print("Interrupt Mask: " + format(interrupt_mask, "08b"))
    print("Value Mask: " + format(value_mask, "08b"))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    io = BrickletIO16(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register interrupt callback to function cb_interrupt
    io.register_callback(io.CALLBACK_INTERRUPT, cb_interrupt)

    # Enable interrupt on pin 2 of port A
    io.set_port_interrupt("a", 1 << 2)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
