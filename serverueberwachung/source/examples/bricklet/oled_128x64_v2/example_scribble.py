#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your OLED 128x64 Bricklet 2.0
WIDTH = 128 # Columns
HEIGHT = 64 # Rows

import math
import time
from PIL import Image, ImageDraw
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_oled_128x64_v2 import BrickletOLED128x64V2

def draw_image(oled, start_column, start_row, column_count, row_count, image):
    image_data = image.load()
    pixels = []

    # Convert image pixels into 8bit pages
    for row in range(row_count):
        for column in range(column_count):
            pixels.append(image_data[column, row] != 0)

    oled.write_pixels(0, 0, WIDTH-1, HEIGHT-1, pixels)

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    oled = BrickletOLED128x64V2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Clear display
    oled.clear_display()

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

            draw_image(oled, 0, 0, WIDTH, HEIGHT, image)
            time.sleep(0.025)

            angle += 1
    except KeyboardInterrupt:
        pass

    ipcon.disconnect()
