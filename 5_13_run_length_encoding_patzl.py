# Christian Patzl 1BHIF
# Run Length Encoding


def encode(s: str) -> str:
    """Run-length encoding

    Args:
        s (str): Der zu kodierende String

    Returns:
        str: Den kodierten String
    """
    count = ""
    current = ""
    out = []
    for i in s:
        if i == current:
            count += 1
        else:
            out.append(current + str(count))
            count = 1
            current = i
    out += current + str(count)
    return "".join(out)


def decode(s: str) -> str:
    """Run-length decoding

    Args:
        s (str): Der zu dekodierende String

    Returns:
        str: Der dekodierte String
    """
    letter = ""
    count = "0"
    out = []
    for i in s:
        if i.isdecimal():
            count += i
        else:
            out.append(letter * int(count))
            letter = i
            count = ""
    out += letter * int(count)
    return "".join(out)

while True:
    eingabe = input("Modusauswahl: (e)ncode, (d)ecode, (Enter) abbrechen: ")
    if eingabe == "e":
        print(encode(input("Text: ")))
    elif eingabe == "d":
        print(decode(input("Text: ")))
    else:
        break
print("Programm beendet")