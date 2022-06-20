from random import choice, randint


with open("files/all_sounds.🗿", encoding="utf-8") as f:
    sounds = f.read().split("|")

newsounds = []
for i in range(1000):
    newsounds.append(f"{choice(sounds)}@{randint(-10, 10)}")

with open("files/30dwbs.🗿", "w", encoding="utf-8") as f:
    f.write("|".join(newsounds))