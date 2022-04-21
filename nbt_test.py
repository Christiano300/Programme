import nbtlib

palette = []
index = 0
index2 = 0
blocks = []



def import_data():
    index = file.find('palette')
    while True:
        index = file.find("minecraft", index + 1)
        if index != -1:
            index2 = file.find('"', index)
            palette.append(file[index + 10:index2])
        else:
            break
    #positions
    index = file.find('blocks')
    while True:
        index = file.find("pos", index + 1)
        if index != -1:
            index2 = file.find(",", index)
            x = int(file[index + 6:index2])

            index = file.find(' ', index2)
            index2 = file.find(',', index)
            y = int(file[index + 1:index2])

            index = index2 + 1
            index2 = file.find(']', index)
            z = int(file[index:index2])
            
            index = file.find('state', index2) + 7
            index2 = file.find('}', index)
            try:
                state = int(file[index:index2])
            except ValueError:
                print(f"ValueError from postion {index} to {index2}:\n" + file[index - 10:index2 + 10] + f"\n{'^':^21s}")
                quit()
            

            blocks.append([x, y, z, palette[state]])
        else:
            break

    index = file.find('size')
    index = file.find('[', index)
    index

def simple_function(name):
    function_text = ""
    for i in blocks:
        function_text = function_text + "setblock ~" + str(i[0] + XOffset) + " ~" + str(i[1] + YOffset) + " ~" + str(i[2] + ZOffset) + " " + i[3] + "\n"
    function_file = open(name + ".mcfunction", 'w')
    function_file.write(function_text)
    function_file.close()
    
def complex_function():
    print("Still to do")

while True:
    filename = input("Enter filename with extension: ")
    try:
        file = nbtlib.serialize_tag(nbtlib.load(filename, gzipped=True))
    except:
        print("Could not find file. Please try again.")
    else:
        break
import_data()
function_name = input("Function Name (Press enter for filename): ")
if function_name == "":
    function_name = filename.rstrip(".nbt")

while True:
    delay = input("Delay between layers(y/n): ")
    if delay == "y":
        delay = int(input("Delay between layers(ticks): "))
        while True:
            if delay > 0:
                simple = False
                break
            else:
                print("Invalid Input. Please try again.")
        break
    elif delay == "n":
        simple = True
        break
    else:
        print("Invalid input. Please try again.")

while True:
    XOffset = input("X Offset: ")
    try:
        XOffset = int(XOffset)
    except:
        print("Invalid Input. Please try again.")
    else:
        break

while True:
    YOffset = input("Y Offset: ")
    try:
        YOffset = int(YOffset)
    except:
        print("Invalid Input. Please try again.")
    else:
        break

while True:
    ZOffset = input("Z Offset: ")
    try:
        ZOffset = int(ZOffset)
    except:
        print("Invalid Input. Please try again.")
    else:
        break


if simple:
    simple_function(function_name)
else:
    complex_function()

"""
{"": {size: [3, 4, 3], entities: [], blocks: [{pos: [0, 0, 0], state: 0}, {pos: [1, 0, 0], state: 0}, {pos: [2, 0, 0], state: 0}, {pos: [0, 0, 1], state: 0}, {pos: [1, 0, 1], state: 0}, {pos: [2, 0, 1], state: 0}, {pos: [0, 0, 2], state: 0}, {pos: [1, 0, 2], state: 0}, {pos: [2, 0, 2], state: 0}, {pos: [0, 1, 0], state: 1}, {pos: [1, 1, 0], state: 1}, {pos: [2, 1, 0], state: 1}, {pos: [0, 2, 0], state: 1}, {pos: [1, 2, 0], state: 1}, {pos: [2, 2, 0], state: 1}, {pos: [0, 3, 0], state: 1}, {pos: [1, 3, 0], state: 1}, {pos: [2, 3, 0], state: 1}, {pos: [0, 1, 1], state: 1}, {pos: [1, 1, 1], state: 1}, {pos: [2, 1, 1], state: 1}, {pos: [0, 2, 1], state: 1}, {pos: [1, 2, 1], state: 1}, {pos: [2, 2, 1], state: 1}, {pos: [0, 3, 1], state: 1}, {pos: [1, 3, 1], state: 1}, {pos: [2, 3, 1], state: 1}, {pos: [0, 1, 2], state: 1}, {pos: [1, 1, 2], state: 1}, {pos: [2, 1, 2], state: 1}, {pos: [0, 2, 2], state: 1}, {pos: [1, 2, 2], state: 1}, {pos: 
[2, 2, 2], state: 1}, {pos: [0, 3, 2], state: 1}, {pos: [1, 3, 2], state: 1}, {pos: [2, 3, 2], state: 1}], palette: [{Name: "minecraft:sandstone"}, {Name: "minecraft:air"}], DataVersion: 1963}}
"""