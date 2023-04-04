#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Real-Time Clock Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_real_time_clock_v2 import BrickletRealTimeClockV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rtc = BrickletRealTimeClockV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current date and time
    year, month, day, hour, minute, second, centisecond, weekday, \
      timestamp = rtc.get_date_time()

    print("Year: " + str(year))
    print("Month: " + str(month))
    print("Day: " + str(day))
    print("Hour: " + str(hour))
    print("Minute: " + str(minute))
    print("Second: " + str(second))
    print("Centisecond: " + str(centisecond))

    if weekday == rtc.WEEKDAY_MONDAY:
        print("Weekday: Monday")
    elif weekday == rtc.WEEKDAY_TUESDAY:
        print("Weekday: Tuesday")
    elif weekday == rtc.WEEKDAY_WEDNESDAY:
        print("Weekday: Wednesday")
    elif weekday == rtc.WEEKDAY_THURSDAY:
        print("Weekday: Thursday")
    elif weekday == rtc.WEEKDAY_FRIDAY:
        print("Weekday: Friday")
    elif weekday == rtc.WEEKDAY_SATURDAY:
        print("Weekday: Saturday")
    elif weekday == rtc.WEEKDAY_SUNDAY:
        print("Weekday: Sunday")

    print("Timestamp: " + str(timestamp) + " ms")

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
