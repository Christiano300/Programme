from PIL import Image
from tqdm import tqdm

im = Image.new("RGB", (4096, 4096))

for red in tqdm(range(256)):
    for green in range(256):
        for blue in range(256):
            im.putpixel((red % 16 * 256 + green, red // 16 * 256 + blue), (red, green, blue))

im.show()