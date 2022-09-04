from PIL import Image, ImageGrab, UnidentifiedImageError

colors = [0x1633b2, 0xea0000, 0xffffff, 0xff7500, 0x25ed1f, 0xf6f511]

colors = [(i >> 16 & 255, i >> 8 & 255, i & 255) for i in colors]

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


data = im.getdata()

new = [min(colors, key=lambda a: sum(abs(x - y) for x, y in zip(a, i))) for i in data]

im.putdata(new)
im.show()