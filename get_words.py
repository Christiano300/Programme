import os


words = []
files = []
for root, dirs, f in os.walk(".."):
    for i in f:
        if i.endswith(".py"):
            files.append(root + "/" + i)

for i in files:
    with open(i, encoding="utf-8") as f:
        text = f.read()
    for word in text.split(" "):
        for word2 in word.split("\n"):
            if word2.isalpha() and len(word2) < 30:
                words.append(word2)

with open("ignfiles/python_text.txt", "w", encoding="utf-8") as f:
    print(" ".join(words), file=f)
print(len(files))
print(len(words))