#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Industrial Counter Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_industrial_counter import BrickletIndustrialCounter

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ic = BrickletIndustrialCounter(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current counter from channel 0
    counter = ic.get_counter(ic.CHANNEL_0)
    print("Counter (Channel 0): " + str(counter))

    # Get current signal data from channel 0
    duty_cycle, period, frequency, value = ic.get_signal_data(ic.CHANNEL_0)

    print("Duty Cycle (Channel 0): " + str(duty_cycle/100.0) + " %")
    print("Period (Channel 0): " + str(period) + " ns")
    print("Frequency (Channel 0): " + str(frequency/1000.0) + " Hz")
    print("Value (Channel 0): " + str(value))

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
