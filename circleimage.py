from math import sqrt
from PIL import Image
from colorsys import hsv_to_rgb

import numpy as np

im = Image.new("RGB", (256, 256))

centerx = centery = 120

data = np.zeros(im.width * im.height)
for x in range(im.width):
    for y in range(im.height):
        v = sqrt((x - centerx) ** 2 + (y - centery) ** 2)
        r, g, b = tuple(int(i * 255) for i in hsv_to_rgb(v / 100 % 1, 1, 1))
        
        data[x * im.width + y] = (r << 16 | g << 8 | b) ^ (g << 16 | b << 8 | r) ^ (b << 16 | r << 8 | g)

im.putdata(list(int(i) for i in data))
im.show()