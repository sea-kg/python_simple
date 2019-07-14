#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw 

print("Hello world!")
thumbnail_size = 50, 50

  
filename = "will-smith-face-png.png"
with Image.open(filename) as img:
    width = img.size[0]
    height = img.size[1]
    print("Width: " + str(width))
    print("Height: " + str(height))

    # Распечатка текста
    text_x = 320
    text_y = 250
    d = ImageDraw.Draw(img)
    font1 = ImageFont.truetype("fonts/Acme-Regular.ttf", 48)
    d.text((text_x, text_y),"Will Smith",(0,0,0),font=font1)
    img.save("text.png")

    # Переворачиваем картинку
    img_rotate = img.rotate(-45)
    img_rotate.save("rotate-45.png", "PNG")
    
    # Делаем thumbnail
    img.thumbnail([50,50])
    img.save("thumbnail50.png", "PNG")

    

