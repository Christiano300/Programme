from math import sqrt
from PIL import Image
from colorsys import hsv_to_rgb

im = Image.new("RGB", (256, 256))

centerx = centery = 120

data = []
for x in range(im.width):
    for y in range(im.height):
        v = sqrt(abs(x - centerx) ** 2 + abs(y - centery) ** 2)
        data.append(tuple([int(i * 255) for i in hsv_to_rgb(v / 100 % 1, 1, 1)]))

im.putdata(data)
im.show()