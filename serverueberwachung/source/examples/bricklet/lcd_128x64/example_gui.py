#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your LCD 128x64 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_128x64 import BrickletLCD128x64

# Callback function for GUI button pressed callback
def cb_gui_button_pressed(index, pressed):
    print("Index: " + str(index))
    print("Pressed: " + str(pressed))
    print("")

# Callback function for GUI slider value callback
def cb_gui_slider_value(index, value):
    print("Index: " + str(index))
    print("Value: " + str(value))
    print("")

# Callback function for GUI tab selected callback
def cb_gui_tab_selected(index):
    print("Index: " + str(index))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lcd = BrickletLCD128x64(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register GUI button pressed callback to function cb_gui_button_pressed
    lcd.register_callback(lcd.CALLBACK_GUI_BUTTON_PRESSED, cb_gui_button_pressed)

    # Register GUI slider value callback to function cb_gui_slider_value
    lcd.register_callback(lcd.CALLBACK_GUI_SLIDER_VALUE, cb_gui_slider_value)

    # Register GUI tab selected callback to function cb_gui_tab_selected
    lcd.register_callback(lcd.CALLBACK_GUI_TAB_SELECTED, cb_gui_tab_selected)

    # Clear display
    lcd.clear_display()
    lcd.remove_all_gui()

    # Add GUI elements: Button, Slider and Graph with 60 data points
    lcd.set_gui_button(0, 0, 0, 60, 20, "button")
    lcd.set_gui_slider(0, 0, 30, 60, lcd.DIRECTION_HORIZONTAL, 50)
    lcd.set_gui_graph_configuration(0, lcd.GRAPH_TYPE_LINE, 62, 0, 60, 52, "X", "Y")

    # Add a few data points (the remaining points will be 0)
    lcd.set_gui_graph_data(0, [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240])

    # Add 5 text tabs without and configure it for click and swipe without auto-redraw
    lcd.set_gui_tab_configuration(lcd.CHANGE_TAB_ON_CLICK_AND_SWIPE, False)
    lcd.set_gui_tab_text(0, "Tab A")
    lcd.set_gui_tab_text(1, "Tab B")
    lcd.set_gui_tab_text(2, "Tab C")
    lcd.set_gui_tab_text(3, "Tab D")
    lcd.set_gui_tab_text(4, "Tab E")

    # Set period for GUI button pressed callback to 0.1s (100ms)
    lcd.set_gui_button_pressed_callback_configuration(100, True)

    # Set period for GUI slider value callback to 0.1s (100ms)
    lcd.set_gui_slider_value_callback_configuration(100, True)

    # Set period for GUI tab selected callback to 0.1s (100ms)
    lcd.set_gui_tab_selected_callback_configuration(100, True)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
