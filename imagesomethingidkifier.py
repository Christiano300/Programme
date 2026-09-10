from pdb import pm
from PIL import Image, ImageGrab, UnidentifiedImageError

while True:
    name = input(
        "Enter Filename with extension (leave empty to read from clipboard): ")
    if name:
        try:
            im = Image.open(name)
        except FileNotFoundError:
            print(f"File '{name}' not found.")
        except UnidentifiedImageError:
            print("Image cannot be opened and identified.")
        else:
            im = im.convert("RGB")
            break
    else:
        im = ImageGrab.grabclipboard()
        if im == None:
            print("Clipboard does not contain an image.")
        elif isinstance(im, Image.Image):
            im = im.convert("RGB")
            break
        elif isinstance(im, list):
            if len(im) > 1:
                print("Clipboard contains more than one image.")
                continue
            try:
                im = Image.open(im[0])
            except FileNotFoundError:
                print("Clipboard does not contain an image.")
            except UnidentifiedImageError:
                print("Image cannot be opened and identified.")
            else:
                im = im.convert("RGB")
                break

data = list(im.getdata())
new: list[int | tuple[int, int, int]] = [0] * (im.width * im.height)

def pmhash(x: int) -> int:
    return round(((hash(str(x)) % 256) - 128))

l = len(data)
for i in range(l):
    channel = hash(str(i)) % 3
    pixel = [0 for j in range(3)]
    pixel[channel] += data[i][channel]
    new[i] = tuple(pixel)
    
im.putdata(new)
im.show()