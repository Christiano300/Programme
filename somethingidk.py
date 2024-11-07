from PIL import Image

im = Image.new("RGB", (128, 128))

data = [0] * (im.width * im.height)

for i in range(len(data)):
    data[i] = (hash(str(i)) % 256, hash(str(i + 1)) % 256, hash(str(i + 2)) % 256)

im.putdata(data)
im.show()