#!/usr/bin/env python3

import glob
from turtle import pos
from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from inky import InkyWHAT
from time import sleep
import os
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

def createCheckbox(position, checked=False):
  width = 30
  small_border_width = 3

  for x in range(position[0], position[0] + width):
    for y in range(position[1], position[1] + width):
        img.putpixel((x, y), inky_display.BLACK)

  if not checked:
    small_width = width - (small_border_width*2)
    small_pos = (position[0] + small_border_width, position[1] + small_border_width)
    for x in range(small_pos[0], small_pos[0] + small_width):
      for y in range(small_pos[1], small_pos[1] + small_width):
        img.putpixel((x, y), inky_display.WHITE)

def addItem(text, position, checked=False):
  item_w, item_h = hanken_medium_font.getsize(text)
  draw.text((50, 40 * position + 60), text, inky_display.BLACK, font=hanken_medium_font)
  createCheckbox((15, 40*position + 65), checked)
    
addItem('Go to school', 0, True)
addItem('Take a walk', 1, True)
addItem('Do homework', 2, False)
addItem('Stop gaming', 3, False)

inky_display.set_image(img)
inky_display.show()
#inky_display.show_stay_awake()