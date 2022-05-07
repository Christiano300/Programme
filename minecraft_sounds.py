import json


def all_one_sound(sounds: dict, sound: str) -> dict:
    replace = sounds[sound]["sounds"]
    print(len(sounds))
    for name in sounds:
        sounds[name]["sounds"] = replace
        sounds[name]["replace"] = True
    return sounds


with open("files/sounds.json", "r") as f:
    sounds = json.load(f)

newsounds = all_one_sound(sounds, "entity.ghast.hurt")
with open("files/newsounds.json", "w") as f:
    json.dump(newsounds, f, indent=4)
