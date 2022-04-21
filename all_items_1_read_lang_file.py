import re
import os

next_is_block = False
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'files\en_us.json')
finalstring = ""
index = 0

with open(filename, "r") as file:
    input_string = file.read()
    file.close()

pattern = re.compile(r'"([^"]+)"')
matches = re.findall(pattern, input_string)
blocks = []

def is_block(block):
    if block.startswith('block.minecraft.banner.'):
        return False
    elif block.endswith('.desc'):
        return False
    elif 'potion.effect' in block or 'arrow.effect' in block:
        return False
    elif 'shield.' in block:
        return False
    elif 'spawn_egg' in block:
        return False
    elif block.startswith('block.minecraft.') or block.startswith('item.minecraft.'):
        return True

for i in matches:
    if next_is_block:
        blocks.append(i)
        print(f"with name: {i}")
        next_is_block = False
    elif is_block(i):
        blocks.append(i)
        print(f"Found item with id: {i} ", end='')
        next_is_block = True

for i in range(int(len(blocks) / 2)):
    finalstring = finalstring +  blocks[index] + "=" + blocks[index + 1] + "\n"
    index += 2

filename = os.path.join(dirname, 'files\only_blocks.txt')
with open(filename, "w") as file:
    file.write(finalstring.rstrip("\n"))