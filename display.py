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

# Get the current path
PATH = os.path.dirname(__file__)

def create_mask(source, mask=(inky_display.WHITE, inky_display.BLACK, inky_display.RED)):
    """Create a transparency mask.
    Takes a paletized source image and converts it into a mask
    permitting all the colours supported by Inky pHAT (0, 1, 2)
    or an optional list of allowed colours.
    :param mask: Optional list of Inky pHAT colours to allow.
    """
    mask_image = Image.new("1", source.size)
    w, h = source.size
    for x in range(w):
        for y in range(h):
            p = source.getpixel((x, y))
            if p in mask:
                mask_image.putpixel((x, y), 255)

    return mask_image

# Dictionaries to store our icons and icon masks in
icons = {}
masks = {}

# Load our icon files and generate masks
for icon in glob.glob(os.path.join(PATH, "resources/*.png")):
  icon_name = icon.split("resources/")[1].replace(".png", "")
  icon_image = Image.open(icon)
  icons[icon_name] = icon_image
  masks[icon_name] = create_mask(icon_image)

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

  if checked:
    print('checked')
  else:
    print('not checked')
    small_width = width - (small_border_width*2)
    small_pos = (position[0] + small_border_width, position[1] + small_border_width)
    for x in range(small_pos[0], small_pos[0] + small_width):
      for y in range(small_pos[1], small_pos[1] + small_width):
        img.putpixel((x, y), inky_display.WHITE)

def addItem(text, position, checked=False):
  item_w, item_h = hanken_medium_font.getsize(text)
  draw.text((50, 40*position + 60), text, inky_display.BLACK, font=hanken_medium_font)
  createCheckbox((0, 40*position + 60), False)
    
addItem('Go to school', 0)
addItem('Go to school', 1)
addItem('Go to school', 2)

print(icons)
print(masks)

img.paste(icons['full-cb'], (100, 100), masks['full-cb'])
img.paste(icons['empty-cb'], (50, 50), masks['empty-cb'])

inky_display.set_image(img)
inky_display.show()
#inky_display.show_stay_awake()