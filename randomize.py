import os
import random
import io
import zipfile
import json
import sys

# Paketname festlegen
if len(sys.argv) >= 2:
	try:
		seed = int(sys.argv[1])
	except Exception:
		print(f'The seed "{sys.argv[1]}" is not an integer.')
		exit()
	random.seed(seed)
	datapack_name = f'random_recipes_{seed}'
	datapack_desc = f'Recipe Randomizer, Seed: {seed}'
else:
	print('If you want to use a specific randomizer seed integer, use: "python randomize.py <seed>"')
	datapack_name = 'random_recipes'
	datapack_desc = 'Recipe Randomizer'
	
datapack_filename = datapack_name + '.zip'

print('Generating datapack...')
	
file_list = []
remaining = []

# Dateipfade speichern
for dirpath, dirnames, filenames in os.walk('recipes'):
	for filename in filenames:
		file_list.append(os.path.join(dirpath, filename))


# Get item and count
for file in file_list:
	f = open(file, 'r')
	filetext = f.read()
	f.close()
	index = filetext.find("result")
	# Check if recipe has a result
	if  index == -1:
		file_list.remove(file)
	else:
		# Find item
		index = filetext.find("item", index) + 8
		index2 = filetext.find('"', index)
		item = filetext[index:index2]
		#Find count
		index = filetext.find("count", index) + 8
		if index == -1:
			count = -1
		else:
			index2 = filetext.find("\n", index)
			count = filetext[index:index2]
		# Save item and count
		remaining.append([item, count])
		
		
file_dict = {}

# Randomize
for file in file_list:
	i = random.randint(0, len(remaining)-1)
	file_dict[file] = remaining[i]
	del remaining[i]
	
zipbytes = io.BytesIO()
zip = zipfile.ZipFile(zipbytes, 'w', zipfile.ZIP_DEFLATED, False)

for from_file in file_dict:
	with open(from_file, "rb") as file:
		contents = file.read()
		
	zip.writestr(os.path.join('data/minecraft/', file_dict[from_file]), contents)
	
zip.writestr('pack.mcmeta', json.dumps({'pack':{'pack_format':1, 'description':datapack_desc}}, indent=4))
zip.writestr('data/minecraft/tags/functions/load.json', json.dumps({'values':['{}:reset'.format(datapack_name)]}))
zip.writestr('data/{}/functions/reset.mcfunction'.format(datapack_name), 'tellraw @a ["",{"text":"Recipe randomizer by SethBling","color":"green"}]')
	
zip.close()
with open(datapack_filename, 'wb') as file:
	file.write(zipbytes.getvalue())
	
print('Created datapack "{}"'.format(datapack_filename))