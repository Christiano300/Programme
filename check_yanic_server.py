import requests
import json

url = "https://api.mcstatus.io/v1/status/java/116.202.217.71"
r = requests.get(url)
j = json.loads(r.text)
online = j['online']
print(f"Server online: {'ja' if online else 'nein'}")
if online:
    if j['response']["players"]["online"]:
        sample = j['response']["players"]["sample"]
        print(f"Spieler: {sample}")
    else:
        print("Niemand online")
