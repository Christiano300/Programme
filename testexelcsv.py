# Christian Patzl 1BHIF
# CSV zu JSON konvertieren

import csv
with open("testexcelcsv.csv") as f:
    reader = csv.DictReader(f, delimiter=";")
    lines = list(reader)
    print(lines)

with open("testexcelcsv.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, lines[0].keys(), dialect='excel', delimiter=";")
    writer.writeheader()
    writer.writerows(lines)