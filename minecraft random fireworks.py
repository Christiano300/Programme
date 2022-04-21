import pyperclip
from random import randint, choice

colors = [
    "1973019", "11743532", "3887386", "5320730", "2437522", "8073150",
    "2651799", "11250603", "4408131", "14188952", "4312372", "14602026",
    "6719955", "12801229", "15435844", "15790320"
]

normalcolors = ",".join([choice(colors) for i in range(randint(1, 16))])
fadecolors = ",".join([choice(colors) for i in range(randint(1, 16))])

flicker = ",Flicker:1" if randint(0, 1) else ""
trail = ",Trail:1" if randint(0, 1) else ""

string = f"/give @s firework_rocket{{Fireworks:{{Flight:1,Explosions:[{{Type:{randint(0, 4)}{flicker}{trail},Colors:[I;{normalcolors}],FadeColors:[I;{fadecolors}]}}]}}}}"
print(string)
pyperclip.copy(string)
