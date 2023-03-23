import re
from google_trans_new import google_translator
tr = google_translator()


with open("files/de_de.txt") as file:
    input_string = file.read()
print("Converting to python...")
input_string = input_string.replace("\\u201e", "„")
input_string = input_string.replace("\\u201c", "“")
input_string = input_string.replace("\\u00e4", "ä")
input_string = input_string.replace("\\u00f6", "ö")
input_string = input_string.replace("\\u00fc", "ü")
input_string = input_string.replace("\\u201a", "‚")
input_string = input_string.replace("\\u2018", "‘")
input_string = input_string.replace("\\u00dc", "Ü")
input_string = input_string.replace("\\u00df", "ß")
input_string = input_string.replace("\\u2026", "…")
input_string = input_string.replace("\\u2019", "’")
input_string = input_string.replace("\\u00d6", "Ö")
input_string = input_string.replace("\\u2010", "‐")
input_string = input_string.replace("\\u2013", "–")
input_string = input_string.replace("\\u00c4", "Ä")
print("Translating...")
input_language = "de"
between_language = "mg"


def translateback(m):
    if not "." in m:
        try:
            t1 = tr.translate(m, lang_tgt=between_language)
            t2 = tr.translate(t1, lang_tgt=input_language)
            return t2
        except Exception as err:
            exception_type = type(err).__name__
            print("An error occured: " + exception_type)
            print("The error was caused here: " + m)
            print(err)
            return m
    else:
        return m


def guenni(s):
    return " ".join(["SUS" for i in s.split()])


pattern = re.compile('(?<=: \")[^\"]*(?=\")')

finalfile = re.sub(pattern, lambda x: guenni(x.group()), input_string)
print("Converting to minecraft...")
finalfile = finalfile.replace("“", "\\u201c")
finalfile = finalfile.replace("ä", "\\u00e4")
finalfile = finalfile.replace("„", "\\u201e")
finalfile = finalfile.replace("ö", "\\u00f6")
finalfile = finalfile.replace("ü", "\\u00fc")
finalfile = finalfile.replace("‚", "\\u201a")
finalfile = finalfile.replace("‘", "\\u2018")
finalfile = finalfile.replace("Ü", "\\u00dc")
finalfile = finalfile.replace("ß", "\\u00df")
finalfile = finalfile.replace("…", "\\u2026")
finalfile = finalfile.replace("’", "\\u2019")
finalfile = finalfile.replace("Ö", "\\u00d6")
finalfile = finalfile.replace("‐", "\\u2010")
finalfile = finalfile.replace("–", "\\u2013")
finalfile = finalfile.replace("Ä", "\\u00c4")

with open("files/de_amogus.txt", "w") as file:
    file.write(finalfile)
