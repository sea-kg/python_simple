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

# Создадим картинку

img1 = Image.new("RGBA", (300,300), (0,0,0,0))

draw1 = ImageDraw.Draw(img1)
x0 = 10
y0 = 10
x1 = 290
y1 = 290
draw1.ellipse([x0, y0, x1, y1], fill="red", outline="red")
draw1.chord([x0, y0, x1, y1], 0, 180, fill="white", outline="white")

draw1.ellipse([100, 100, 200, 200], fill="black", outline="black")
draw1.ellipse([110, 110, 190, 190], fill="white", outline="white")
draw1.line([
    (10,10),
    (50,50),
    (50,90),
    (10,140)
], fill="yellow", width=10)


draw1.polygon([
    (10,10),
    (50,50),
    (50,90),
    (10,140)
], fill="green", outline="black")

img1.save("new320x320.png", "PNG")


    

