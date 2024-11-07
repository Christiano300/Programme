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

colors = {(255, 255, 255): ".", (0, 0, 0): "X",
          (0, 0, 255): "o", (255, 0, 0): " "}
strings = []
pixels = im.getdata()
for i in range(im.size[1]):
    line = []
    for j in range(im.size[0]):
        line.append(colors[pixels[i * im.size[0] + j]])
    strings.append("".join(line))
print("_custom_cursor_ = (\"", "\",\n\"".join(strings), "\")", sep="")
print("pygame.cursors.compile(_custom_cursor_, black='X', white='.', xor='o')")
