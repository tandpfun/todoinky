#!/usr/bin/env python3

import argparse

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from inky import InkyWHAT
from time import sleep
try:
    inky_display = InkyWHAT('black')
    #inky_display = inky_fast.InkyPHATFast("black")
except TypeError:
    raise TypeError("You need to update the Inky library to >= v1.1.0")

# Figure out scaling for display size

scale_size = 1.0
padding = 0

if inky_display.resolution == (400, 300):
    scale_size = 2.20
    padding = 5

if inky_display.resolution == (600, 448):
    scale_size = 2.20
    padding = 10

if inky_display.resolution == (250, 122):
    scale_size = 1.30
    padding = -5

# Create a new canvas to draw on

img = Image.new("P", inky_display.resolution)
draw = ImageDraw.Draw(img)

# Load the fonts

intuitive_font = ImageFont.truetype(Intuitive, int(22 * scale_size))
hanken_bold_font = ImageFont.truetype(HankenGroteskBold, int(22 * scale_size))
hanken_medium_font = ImageFont.truetype(HankenGroteskMedium, int(16 * scale_size))

y_top = int(inky_display.height * (5.0 / 10.0))
y_bottom = y_top + int(inky_display.height * (4.0 / 10.0))

        
# Calculate the positioning and draw the "Hello" text

title_w, title_h = hanken_bold_font.getsize("TodoInky")
# hello_x = int((inky_display.width - hello_w) / 2)
title_x = 5
title_y = 0
draw.text((title_x, title_y), "TodoInky", inky_display.BLACK, font=hanken_bold_font)

#inky_display.show_stay_awake()

def addItem(text, position):
    item_w, item_h = hanken_medium_font.getsize(text)
    draw.text((50, 40*position + 60), text, inky_display.BLACK, font=hanken_medium_font)
    
addItem('Go to school', 0)
addItem('Go to school', 1)
addItem('Go to school', 2)

inky_display.set_image(img)
inky_display.show()
#inky_display.show_stay_awake()

