import requests
import json

# ip = "play.hypixel.net"
# ip = "116.202.217.71"
ip = "pc.einfachnurmaxi.de"
url = "https://api.mcstatus.io/v1/status/java/" + ip
r = requests.get(url)
j = json.loads(r.text)
online = j['online']
if online:
    print("Server online")
    if j['response']["players"]["online"]:
        print(f'{j["response"]["players"]["online"]} / {j["response"]["players"]["max"]} Spielern')
        sample = j['response']["players"]["sample"]
        if sample:
            print(f"Spieler: {', '.join((i['name'] for i in sample))}")
    else:
        print("Niemand online")
else:
    print("Server nicht online")
