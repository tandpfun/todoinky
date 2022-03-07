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

#inky_display.show_stay_awake()

def clearDisplay():
  for x in range(0, inky_display.width):
    for y in range(0, inky_display.height):
        img.putpixel((x, y), inky_display.WHITE)

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
  draw.text((50, 40 * position + 60), text, inky_display.BLACK, font=hanken_medium_font)
  createCheckbox((15, 40*position + 65), checked)
    
def showItems(items):
  print(items)
  clearDisplay()
  
  draw.text((5, 0), "TodoInky", inky_display.BLACK, font=hanken_bold_font)

  i = 0
  for item in items:
    print(item)
    addItem(item.name, i, item.checked)
    i = i+1
  inky_display.set_image(img)
  inky_display.show()