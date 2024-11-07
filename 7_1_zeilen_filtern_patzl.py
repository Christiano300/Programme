# Christian Patzl 1BHIF
# Zeilen filtern

def filter_lines(lines: list, pattern: str) -> list:
    """Bekommt eine Liste von Strings übergeben und
    retourniert nur jene Strings, welche das übergebene pattern enthalten"""
    return filter(lambda x: pattern in x, lines)


file = open("Nationalratswahl2017.csv", "r")
lines = [line.rstrip() for line in file.readlines()]
file.close()
filtered = filter_lines(lines, "Pölten")
for line in filtered:
    print(line)
