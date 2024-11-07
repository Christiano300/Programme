import csv

with open("files/kundenliste_vorher.csv", encoding="utf-8-sig") as f, \
    open("files/kundenliste_nachher.csv", "w", newline="", encoding="utf-8-sig") as fn:
    reader = csv.DictReader(f, delimiter=";")
    writer = csv.DictWriter(fn, delimiter=";", fieldnames=["Nachname", "Vorname", "Strasse Nr", "PLZ", "Ort", "Telefonnummer", "Geburtstag"])
    writer.writeheader()
    for line in reader:
        line['Nachname'], line['Vorname']= line.pop("Name").split()[:0:-1]
        line.pop('Benutzer')
        line['PLZ'], line['Ort'] = line.pop('PLZ Ort').title().split()
        line.pop('E-Mail-Adresse')
        line['Telefonnummer'] = f"+{line.pop('Länderwahl')} {line.pop('Handynummer')[1:]}"
        line['Geburtstag'] = ".".join([(geb := line['Geburtstag'].split('/'))[1], geb[0], geb[2]]) if "/" in line['Geburtstag'] else line['Geburtstag']
        writer.writerow(line)
        