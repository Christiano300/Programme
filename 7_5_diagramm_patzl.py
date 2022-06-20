# Christian Patzl 1BHIF
# Codeergänzung

import matplotlib.pyplot as plt
import numpy as np

def get_data() -> tuple:
    """Liefert im Tupel(Abgegebene Stimmen, [% der  Stimmen],
    [Parteien] die Ergebnisse der Nationalratswahl 2017."""
    with open("Nationalratswahl2017.csv") as f:
        parteien = f.readline().split(';')[6:12]
        daten = f.readline().split(';')
        return (ges := int(daten[3])), [int(daten[i]) / ges * 100 for i in range(6, 12)], parteien
        

(total_votes, percent, parties) = get_data()
x_axis = np.arange(6)
plt.figure(dpi=400, figsize=(6, 4))
plot = plt.bar(x_axis, height=percent, color=[
               "red", "black", "blue", "green", "pink", "olive"])
plt.xticks(x_axis, parties)
plt.title("Ergebnisse der Nationalratswahl 2017")
plt.ylabel("Prozent der abgegebenen Stimmen")
plt.show()