# from random import randint
# from tqdm import tqdm

# gesamt = 2500000
# kleiner = 0
# for i in tqdm(range(gesamt)):
#     zahl1 = randint(0, 2)
#     zahl2 = randint(0, 2)
#     if int(zahl1 == 2) + int(zahl2 == 2) % 2:
#         kleiner += 1
# print(f"{kleiner / gesamt * 100:.5f}%")

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("loop finished")