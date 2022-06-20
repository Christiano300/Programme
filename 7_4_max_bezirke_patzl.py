# Christian Patzl 1BHIF
# Für jede Partei die Bezirke mit den maximalen relativen stimmen suchen

with open("Nationalratswahl2017.csv") as f:
    header = f.readline().rstrip().split(";")
    parteien = {i: {'max': -1, 'max_bezirk': None} for i in header[6:-1]}
    daten = ({i: j for i, j in zip(header, line.rstrip().split(";"))} for line in f)
    for line in daten:
        ges = int(line['Abgegebene'])
        if ges:
            for i in parteien:
                if line[i] and (anteil := int(line[i]) / ges) > parteien[i]['max']:
                        parteien[i]['max'] = anteil
                        parteien[i]['max_bezirk'] = line['Gebietsname']

for i in parteien:
    print(f"{i:5s} | {parteien[i]['max'] * 100:05.2f} % | {parteien[i]['max_bezirk']}")