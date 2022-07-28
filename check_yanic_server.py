import requests
import json

url = "https://api.mcstatus.io/v1/status/java/116.202.217.71"
r = requests.get(url)
j = json.loads(r.text)
online = j['online']
if online:
    print("Server online")
    if j['response']["players"]["online"]:
        sample = j['response']["players"]["sample"]
        print(f"Spieler: {', '.join((i['name'] for i in sample))}")
    else:
        print("Niemand online")
else:
    print("Server nicht online")
