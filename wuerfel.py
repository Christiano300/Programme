import matplotlib.pyplot as plt
from math import factorial

varianten = {}

def rechne(n, summe_bisher=0, groesstes = 1):
    if n > 0:
        for i in range(groesstes, 7):
            rechne(n - 1, summe_bisher + i, i)
    else:
        varianten[summe_bisher] = varianten.get(summe_bisher, 0) + 1

n = 2
rechne(n)
for k, v in varianten.items():
    varianten[k] *= factorial(n)


plt.plot(list(varianten.keys()), list(varianten.values()))
plt.ylabel('some numbers')
plt.show()

print("\n".join(f"{k}: {v}" for k, v in varianten.items()))