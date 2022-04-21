import os
import time

n = 0
survival_blocks = ""
non_survival_blocks = ""
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'files\only_blocks.txt')
file = open(filename, 'r')
filelines = file.readlines()
file.close()

for i in filelines:
    n  += 1
    is_block = input(str(n) + " of " + str(len(filelines)) + ": " + i.rstrip("\n").replace("=", " ") + ": ")
    time.sleep(0.2)
    if is_block == "":
        survival_blocks += i
    else:
        non_survival_blocks += i

file.close()

filename = os.path.join(dirname, 'files\\survival_blocks.txt')
file = open(filename, 'w')
file.write(survival_blocks)
file.close()

filename = os.path.join(dirname, 'files\\non_survival_blocks.txt')
file = open(filename, 'w')
file.write(non_survival_blocks)
file.close()