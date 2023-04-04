#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Real-Time Clock Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_real_time_clock import BrickletRealTimeClock

# Callback function for date and time callback
def cb_date_time(year, month, day, hour, minute, second, centisecond, weekday, timestamp):
    print("Year: " + str(year))
    print("Month: " + str(month))
    print("Day: " + str(day))
    print("Hour: " + str(hour))
    print("Minute: " + str(minute))
    print("Second: " + str(second))
    print("Centisecond: " + str(centisecond))

    if weekday == BrickletRealTimeClock.WEEKDAY_MONDAY:
        print("Weekday: Monday")
    elif weekday == BrickletRealTimeClock.WEEKDAY_TUESDAY:
        print("Weekday: Tuesday")
    elif weekday == BrickletRealTimeClock.WEEKDAY_WEDNESDAY:
        print("Weekday: Wednesday")
    elif weekday == BrickletRealTimeClock.WEEKDAY_THURSDAY:
        print("Weekday: Thursday")
    elif weekday == BrickletRealTimeClock.WEEKDAY_FRIDAY:
        print("Weekday: Friday")
    elif weekday == BrickletRealTimeClock.WEEKDAY_SATURDAY:
        print("Weekday: Saturday")
    elif weekday == BrickletRealTimeClock.WEEKDAY_SUNDAY:
        print("Weekday: Sunday")

    print("Timestamp: " + str(timestamp))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rtc = BrickletRealTimeClock(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register date and time callback to function cb_date_time
    rtc.register_callback(rtc.CALLBACK_DATE_TIME, cb_date_time)

    # Set period for date and time callback to 5s (5000ms)
    # Note: The date and time callback is only called every 5 seconds
    #       if the date and time has changed since the last call!
    rtc.set_date_time_callback_period(5000)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
