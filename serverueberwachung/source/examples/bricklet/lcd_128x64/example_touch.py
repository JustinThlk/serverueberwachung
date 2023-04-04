#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your LCD 128x64 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_128x64 import BrickletLCD128x64

# Callback function for touch position callback
def cb_touch_position(pressure, x, y, age):
    print("Pressure: " + str(pressure))
    print("X: " + str(x))
    print("Y: " + str(y))
    print("Age: " + str(age))
    print("")

# Callback function for touch gesture callback
def cb_touch_gesture(gesture, duration, pressure_max, x_start, x_end, y_start, y_end,
                     age):
    if gesture == BrickletLCD128x64.GESTURE_LEFT_TO_RIGHT:
        print("Gesture: Left To Right")
    elif gesture == BrickletLCD128x64.GESTURE_RIGHT_TO_LEFT:
        print("Gesture: Right To Left")
    elif gesture == BrickletLCD128x64.GESTURE_TOP_TO_BOTTOM:
        print("Gesture: Top To Bottom")
    elif gesture == BrickletLCD128x64.GESTURE_BOTTOM_TO_TOP:
        print("Gesture: Bottom To Top")

    print("Duration: " + str(duration))
    print("Pressure Max: " + str(pressure_max))
    print("X Start: " + str(x_start))
    print("X End: " + str(x_end))
    print("Y Start: " + str(y_start))
    print("Y End: " + str(y_end))
    print("Age: " + str(age))
    print("")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lcd = BrickletLCD128x64(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register touch position callback to function cb_touch_position
    lcd.register_callback(lcd.CALLBACK_TOUCH_POSITION, cb_touch_position)

    # Register touch gesture callback to function cb_touch_gesture
    lcd.register_callback(lcd.CALLBACK_TOUCH_GESTURE, cb_touch_gesture)

    # Set period for touch position callback to 0.1s (100ms)
    lcd.set_touch_position_callback_configuration(100, True)

    # Set period for touch gesture callback to 0.1s (100ms)
    lcd.set_touch_gesture_callback_configuration(100, True)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
