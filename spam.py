from random import randint
a = []
for i in range(100000):
    for j in range(250):
        a.append(str(randint(0, 1)))
    print("".join(a))
    a = []
