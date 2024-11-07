import os
import re
pattern = re.compile("\n[^\n]")
ges = 0
files = []
for root, dirs, f in os.walk(".."):
    for i in f:
        files.append(root + "/" + i)
dateien = [i for i in files if i.endswith('.py') and not i[i.rfind("/") + 1].isdecimal()]
print(dateien)
for i in dateien:
    with open(i, "r", encoding='utf-8') as f:
        ges += len(re.findall(pattern, f.read()))
print(ges)