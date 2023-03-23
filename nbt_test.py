import nbtlib
import tqdm
color_lut = ["white", "orange", "magenta", "light_blue", "yellow", "lime", "pink",
             "gray", "light_gray", "cyan", "purple", "blue", "brown", "green", "red", "black"]


def inputInt(text: str) -> int:
    while True:
        try:
            a = input(text)
            if a == "":
                return 0
            else:
                return int(a)
        except ValueError:
            print("Must be a whole number")


def import_data(file):
    global palette
    palette = []
    print("Getting palette...")
    for i in tqdm.tqdm(file['palette']):
        props = []
        if i.get('Properties'):
            for prop in i['Properties']:
                if prop == "variant":
                    if "log" in i['Name'].lower():
                        name = i['Properties'][prop] + "_log"
                    elif "planks" in i['Name'].lower():
                        name = i['Properties'][prop] + "_planks"
                    else:
                        continue
                    break
                elif prop == "type":
                    name = i['Properties'][prop]
                    break
                elif prop == "color" and not "wool" in i['Name']:
                    if "stained_hardened_clay" in i['Name'].lower():
                        name = ("light_gray" if i['Properties']['color'] == "silver" else i[
                            'Properties']['color']) + "_terracotta"
                        break
                elif prop == "color":
                    pass
                else:
                    props.append([prop, i['Properties'][prop]])
            else:
                name = i['Name']
        else:
            name = i['Name']
        name = name.replace("minecraft:", "")
        if name == "melon_block":
            name = "melon"
        elif name == "brick_block":
            name = "bricks"
        elif name == "stonebrick":
            name = "stone_bricks"
        elif name == "nether_brick":
            name = "nether_bricks"
        elif name == "hardened_clay":
            name = "terracotta"

        if props:
            palette.append(
                f"{name}[{','.join([f'{i[0]}={i[1]}' for i in props])}]")
        else:
            palette.append(name)
    data = file.get("Data")
    if data != None:
        blocks = []
        print("Processing blocks...")
        for i, block in tqdm.tqdm(enumerate(file['blocks'])):
            if palette[block['state']] in "concrete_powder":
                blockdata = data[i]
                if palette[block['state']] in ["concrete", "concrete_powder", "terracotta"]:
                    blocks.append(
                        [*block['pos'], block['state'], blockdata])
            else:
                blocks.append([*block['pos'], block['state']])
        return blocks
    else:
        return [[*i['pos'], i['state']] for i in file['blocks']]


def write_function(name, delay=0):
    air = palette.index("air") if "air" in palette else -1
    if delay:
        print("WIP")
    else:
        print("Writing function")
        function_lines = []
        for i in blocks:
            color = color_lut[i[4]] + "_" if len(i) == 5 else ""
            color = color_lut[i[4]] + "_" if len(i) == 5 else ""
            if i[3] != air:
                function_lines.append(
                    f"setblock ~{i[0] + XOffset} ~{i[1] + YOffset} ~{i[2] + ZOffset} {color + palette[i[3]]}")
        with open(name + ".mcfunction", 'w') as f:
            f.write("\n".join(function_lines))
        print("Finished writing function")


while True:
    filename = input("Enter filename with extension: ")
    print("Loading file ...")
    try:
        file = nbtlib.load(filename, gzipped=True)
        print("File loaded successfully")
        break
    except FileNotFoundError:
        print("Could not find file. Please try again.")

with open("ignfiles/nbt.txt", "w") as f:
    f.write(nbtlib.serialize_tag(file))

blocks = import_data(file)
function_name = input("Function Name (Press enter for filename): ")
if function_name == "":
    function_name = filename[:-4]

while True:
    do_delay = input("Delay between layers (y/N): ").lower()
    if do_delay == "y":
        while True:
            delay = inputInt("Delay between layers(ticks): ")
            if delay > 0:
                break
            print("Delay must be greater than zero")

    elif do_delay in ("", "n"):
        delay = 0
        break
    else:
        print("Choose a valid option")

XOffset = inputInt("X Offset: ")
YOffset = inputInt("Y Offset: ")
ZOffset = inputInt("Z Offset: ")

write_function(function_name, delay)
"""
{"": {size: [3, 4, 3], entities: [], blocks: [{pos: [0, 0, 0], state: 0}, {pos: [1, 0, 0], state: 0}, {pos: [2, 0, 0], state: 0}, {pos: [0, 0, 1], state: 0}, {pos: [1, 0, 1], state: 0}, {pos: [2, 0, 1], state: 0}, {pos: [0, 0, 2], state: 0}, {pos: [1, 0, 2], state: 0}, {pos: [2, 0, 2], state: 0}, {pos: [0, 1, 0], state: 1}, {pos: [1, 1, 0], state: 1}, {pos: [2, 1, 0], state: 1}, {pos: [0, 2, 0], state: 1}, {pos: [1, 2, 0], state: 1}, {pos: [2, 2, 0], state: 1}, {pos: [0, 3, 0], state: 1}, {pos: [1, 3, 0], state: 1}, {pos: [2, 3, 0], state: 1}, {pos: [0, 1, 1], state: 1}, {pos: [1, 1, 1], state: 1}, {pos: [2, 1, 1], state: 1}, {pos: [0, 2, 1], state: 1}, {pos: [1, 2, 1], state: 1}, {pos: [2, 2, 1], state: 1}, {pos: [0, 3, 1], state: 1}, {pos: [1, 3, 1], state: 1}, {pos: [2, 3, 1], state: 1}, {pos: [0, 1, 2], state: 1}, {pos: [1, 1, 2], state: 1}, {pos: [2, 1, 2], state: 1}, {pos: [0, 2, 2], state: 1}, {pos: [1, 2, 2], state: 1}, {pos: 
[2, 2, 2], state: 1}, {pos: [0, 3, 2], state: 1}, {pos: [1, 3, 2], state: 1}, {pos: [2, 3, 2], state: 1}], palette: [{Name: "minecraft:sandstone"}, {Name: "minecraft:air"}], DataVersion: 1963}}
"""
