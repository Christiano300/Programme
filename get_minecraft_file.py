import os
import json
import shutil

path = os.getenv('APPDATA') + "/.minecraft/assets"
versions = [i.rstrip(".json") for i in os.listdir(
    path + "/indexes") if i.startswith("1.")]
print("Available versions:", *versions, sep="\n")
while True:
    user_input = input("Select a version: ")
    selection = user_input if user_input else max(versions, key=lambda x: int(x.split(".")[-1]))
    print(selection)
    if selection in versions:
        break
    print("Version not available")

with open(f"{path}/indexes/{selection}.json") as f:
    objects = json.load(f)['objects']

while True:
    objectpath = "minecraft/" + input("Enter object path: ")
    if objectpath in objects:
        object = objects[objectpath]
        del objects
        break
    print("Object not found: " + objectpath)

src = f"{path}/objects/{object['hash'][:2]}/{object['hash']}"
dest = f"./files/{objectpath[objectpath.rfind('/') + 1:]}"

shutil.copyfile(src, dest)