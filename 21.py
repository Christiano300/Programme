import tqdm
def d(n):
    summe = 1
    i = 2
    while i * 2 - 1 <= n:
        if  n % i == 0:
            summe += i
        i += 1
    return summe

zahlen = {}
gesamtsumme = 0
for i in tqdm.tqdm(range(1, 10001)):
    zahlen[i] = d(i)
for i in list(zahlen.keys()):
    try:
        if i == zahlen[zahlen[i]] and i != zahlen[i]:
            gesamtsumme += i
    except: pass
print(gesamtsumme)
"""dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'files\en_us.json')"""