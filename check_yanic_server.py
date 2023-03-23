import requests
import json

# ip = "play.hypixel.net"
# ip = "116.202.217.71"
# ip = "pc.einfachnurmaxi.de"
# ip = "185.249.198.148:7001"
ip = "ENMGaming.de:25576"
url = "https://api.mcstatus.io/v1/status/java/" + ip
r = requests.get(url)
j = json.loads(r.text)
online = j['online']
if online:
    print("Server online")
    players = j["response"]["players"]
    if players["online"]:
        print(f'{players["online"]} / {players["max"]} Spieler')
        sample = players["sample"]
        if sample:
            print(f"Spieler: {', '.join((i['name'] for i in sample))}")
    else:
        print("Niemand online")
else:
    print("Server nicht online")
