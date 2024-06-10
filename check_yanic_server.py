import requests
import json
import beaupy
import beaupy.spinners as spinners
from rich.console import Console


with open("files/servers.json") as f:
    servers: dict[str, str] = json.load(f)

console = Console()
console.print("Server: ")
server = beaupy.select(list(servers.keys()))

ip = servers[server] # type: ignore

spinner = spinners.Spinner(spinners.CLOCK)
spinner.start()
res = json.loads(requests.get("https://api.mcstatus.io/v2/status/java/" + ip).text)
spinner.stop()
online = res['online']
if online:
    print("Server online")
    print(f"Mods: {len(res['mods'])}")
    print(f"Plugins: {len(res['plugins'])}")
    players = res["players"]
    if players["online"]:
        print(f'{players["online"]} / {players["max"]} Spieler')
        sample = players.get("list")
        if sample:
            print(f"Spieler: {', '.join((i['name_clean'] for i in sample))}")
    else:
        print("Niemand online")
else:
    print("Server nicht online")