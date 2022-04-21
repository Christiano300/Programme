import re

pattern = r"(\[|\])-?\d+(\.)?(?(2)\d+);-?\d+(\.)?(?(3)\d+)(\[|\])"
wh = True
while wh:
    inputstring = input("Intervallrechnung eingeben: ")
    matches = re.finditer(pattern, inputstring)
    intervals = []
    for match in matches:
        intervals.append(match.group())
    if len(intervals) == 2:
        print(*intervals)
    else:
        print("Ungültige Eingabe. Bitte erneut versuchen")
