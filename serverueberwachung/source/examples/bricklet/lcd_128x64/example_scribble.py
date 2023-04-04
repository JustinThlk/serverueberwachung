#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your LCD 128x64 Bricklet
WIDTH = 128 # Columns
HEIGHT = 64 # Rows

import math
import time
from PIL import Image, ImageDraw
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_lcd_128x64 import BrickletLCD128x64

def draw_image(lcd, start_column, start_row, column_count, row_count, image):
    image_data = image.load()
    pixels = []

    # Convert image pixels into 8bit pages
    for row in range(row_count):
        for column in range(column_count):
            pixels.append(image_data[column, row] != 0)

    lcd.write_pixels(0, 0, WIDTH-1, HEIGHT-1, pixels)

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    lcd = BrickletLCD128x64(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Clear display
    lcd.clear_display()

    # Draw rotating line
    image = Image.new("1", (WIDTH, HEIGHT), 0)
    draw = ImageDraw.Draw(image)
    origin_x = WIDTH // 2
    origin_y = HEIGHT // 2
    length = HEIGHT // 2 - 2
    angle = 0

    print("Press ctrl+c to exit")

    try:
        while True:
            radians = math.pi * angle / 180.0
            x = (int)(origin_x + length * math.cos(radians))
            y = (int)(origin_y + length * math.sin(radians))

            draw.rectangle((0, 0, WIDTH, HEIGHT), 0, 0)
            draw.line((origin_x, origin_y, x, y), 1, 1)

            draw_image(lcd, 0, 0, WIDTH, HEIGHT, image)
            time.sleep(0.025)

            angle += 1
    except KeyboardInterrupt:
        pass

    ipcon.disconnect()
