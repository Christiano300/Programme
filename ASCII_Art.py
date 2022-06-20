from PIL import Image

path = "C:/Users/Christian/Pictures/paint.net/"
file = "sanic.png"
filepath = path + file


greyscale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
l = len(greyscale) - 1
# 1 Buchstabe ist 8 Pixel breit und 18 Pixdel hoch

while True:
    try:
        im = Image.open(path + input("File name: "), 'r').convert("RGBA")
    except FileNotFoundError:
        print(
            f"Datei {file} konnte im Verzeichnis \"{path}\" nicht gefunden werden")
    except PermissionError:
        print("Der Zugriff wurde verweigert oder die Datei konnte nicht gefunden werden")
    else:
        break

inverted = bool(input("Invert Image? "))
if inverted:
    greyscale = greyscale[::-1]
width, height = im.size
im = im.resize((width, round(height / 2)),  Image.Resampling.NEAREST)
width, height = im.size
# List of (R,G,B) Tuples -- RGB values are from 0 to 255
pixel_values = list(im.getdata())
out = []
for i, p in enumerate(pixel_values):
    if i % width == 0:
        out.append("\n")
    g = sum(p[:3]) / 3
    out.append(greyscale[int(g / 255 * l)])

out = "".join(out)
name = input("Enter File save name (leave empty for output): ")
if name:
    with open(name + ".txt", 'w') as f:
        f.write(out)
else:
    print(out)
