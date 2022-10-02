import os
path = input("Path: ")

for i in os.listdir(path):
    name, ext = os.path.splitext(i)
    print("\n" + name)
    new = input("New Name: ").replace(" ", "_")
    orig = os.path.join(path, i)
    renamed = os.path.join(path, new) + "_Patzl" + ext
    os.rename(orig, renamed)