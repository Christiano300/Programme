import pyperclip

dictionary = {18: 20, 20: 26, 26: 24, 24: 18, 19: 23, 23: 25, 25: 21, 21: 19}
keys = list(dictionary.keys())
dictionary_new = {}

for i in keys:
    dictionary_new[dictionary[i]] = i
pyperclip.copy(str(dictionary_new))
print(dictionary_new)