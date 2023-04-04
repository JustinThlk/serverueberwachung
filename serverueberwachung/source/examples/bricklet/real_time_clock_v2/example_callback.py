#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Real-Time Clock Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_real_time_clock_v2 import BrickletRealTimeClockV2

# Callback function for date and time callback
def cb_date_time(year, month, day, hour, minute, second, centisecond, weekday, timestamp):
    print("Year: " + str(year))
    print("Month: " + str(month))
    print("Day: " + str(day))
    print("Hour: " + str(hour))
    print("Minute: " + str(minute))
    print("Second: " + str(second))
    print("Centisecond: " + str(centisecond))

    if weekday == BrickletRealTimeClockV2.WEEKDAY_MONDAY:
        print("Weekday: Monday")
    elif weekday == BrickletRealTimeClockV2.WEEKDAY_TUESDAY:
        print("Weekday: Tuesday")
    elif weekday == BrickletRealTimeClockV2.WEEKDAY_WEDNESDAY:
        print("Weekday: Wednesday")
    elif weekday == BrickletRealTimeClockV2.WEEKDAY_THURSDAY:
        print("Weekday: Thursday")
    elif weekday == BrickletRealTimeClockV2.WEEKDAY_FRIDAY:
        print("Weekday: Friday")
    elif weekday == BrickletRealTimeClockV2.WEEKDAY_SATURDAY:
        print("Weekday: Saturday")
    elif weekday == BrickletRealTimeClockV2.WEEKDAY_SUNDAY:
        print("Weekday: Sunday")

    print("Timestamp: " + str(timestamp))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rtc = BrickletRealTimeClockV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register date and time callback to function cb_date_time
    rtc.register_callback(rtc.CALLBACK_DATE_TIME, cb_date_time)

    # Set period for date and time callback to 5s (5000ms)
    rtc.set_date_time_callback_configuration(5000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
