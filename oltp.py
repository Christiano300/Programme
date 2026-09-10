import random
from datetime import datetime, timedelta

NUM_KATEGORIEN = 9
NUM_LIEFERANTEN = 15
NUM_PERSONAL = 15
NUM_KUNDEN = 45
NUM_ARTIKEL = 30
NUM_FIRMEN = 3
NUM_BESTELLUNGEN = 300
NUM_DETAILS = 900


first_names = [
    "Anna", "Lukas", "Marie", "Paul", "Julia", "Leon", "Sofia", "David", "Laura", "Daniel",
    "Emma", "Noah", "Lisa", "Jonas", "Elena", "Marco", "Mateo", "Eva", "Felix", "Simon"
]

last_names = [
    "Müller", "Huber", "Novak", "Rossi", "Schmidt", "Garcia", "Kowalski",
    "Horvat", "Popescu", "Bianchi", "Weber", "Gruber", "Fischer", "Nowak", "Silva"
]

cities = [
    ("Wien", "Austria"),
    ("Graz", "Austria"),
    ("Berlin", "Germany"),
    ("Munich", "Germany"),
    ("Paris", "France"),
    ("Lyon", "France"),
    ("Madrid", "Spain"),
    ("Barcelona", "Spain"),
    ("Milan", "Italy"),
    ("Rome", "Italy"),
    ("Prague", "Czechia"),
    ("Warsaw", "Poland"),
    ("Budapest", "Hungary"),
    ("Brussels", "Belgium"),
    ("Amsterdam", "Netherlands")
]

streets = [
    "Bahnhofstraße", "Hauptstraße", "Parkstraße", "Ringstraße", "Schulstraße",
    "Kirchgasse", "Bergstraße", "Lindenweg", "Gartenstraße", "Marktplatz"
]

positions = ["Manager", "Sales", "Purchasing", "Coordinator", "Director"]

categories = [
    "Electronics", "Food", "Beverages", "Office", "Sports",
    "Cosmetics", "Household", "Tools", "Toys"
]

product_prefix = [
    "Premium", "Classic", "Eco", "Smart", "Ultra", "Pro", "Compact", "Fresh"
]

shipping_companies = ["DHL", "UPS", "DPD"]


def rand_phone():
    return f"+{random.randint(30, 49)} {random.randint(100000000, 999999999)}"


def rand_street():
    return f"{random.choice(streets)} {random.randint(1, 120)}"


def rand_plz():
    return str(random.randint(1000, 99999))


def rand_date():
    days = random.randint(0, 36*30)
    d = datetime.now() - timedelta(days=days)
    return d.strftime("%Y-%m-%d")


def rand_price():
    price = random.normalvariate(50, 15)
    return round(max(1, price), 2)


def rand_city():
    return random.choice(cities)

# Kategorie
values = []
for c in categories[:NUM_KATEGORIEN]:
    values.append(f"('{c}','Category {c}')")

print("TRUNCATE TABLE oltp.Kategorie;")
print("INSERT INTO oltp.Kategorie (name,beschreibung) VALUES")
print(",\n".join(values) + ";\n")

# Lieferant
values = []
for _ in range(NUM_LIEFERANTEN):

    first = random.choice(first_names)
    last = random.choice(last_names)
    city, country = rand_city()

    firma = f"{last} Trading"
    kontakt = f"{first} {last}"

    values.append(
        f"""('{firma}','{kontakt}','Sales','{rand_street()}','{city}','{city}','{rand_plz()}','{country}','{rand_phone()}','{rand_phone()}')"""
    )

print("TRUNCATE TABLE oltp.Lieferant;")
print("""INSERT INTO oltp.Lieferant
(firma,kontakt,position,strasse,ort,region,plz,land,telefon,telefax) VALUES""")
print(",\n".join(values) + ";\n")

# Versandfirmen
values = [f"('{c}')" for c in shipping_companies]

print("TRUNCATE TABLE oltp.Firma;")
print("INSERT INTO oltp.Firma (name) VALUES")
print(",\n".join(values) + ";\n")

# Personal
values = []
for i in range(NUM_PERSONAL):

    first = random.choice(first_names)
    last = random.choice(last_names)
    city, country = rand_city()

    birth = datetime.now() - timedelta(days=random.randint(9000, 20000))
    hire = datetime.now() - timedelta(days=random.randint(100, 3000))
    
    vorgesetzt = random.randint(1, i) if i > 0 else "NULL"

    values.append(
        f"""('{last}','{first}','{random.choice(positions)}','{birth.date()}','{hire.date()}',
'{rand_street()}','{city}','{city}','{rand_plz()}','{country}',
'{rand_phone()}','{rand_phone()}',NULL,{vorgesetzt})""".replace("\n", "")
    )

print("TRUNCATE TABLE oltp.Personal;")
print("""INSERT INTO oltp.Personal
(nachname,vorname,position,geburtsdatum,einstelldatum,strasse,ort,region,plz,land,tel_privat,tel_buero,bemerkung,vorgesetzt)
VALUES""")
print(",\n".join(values) + ";\n")

# Kunden
values = []
for _ in range(NUM_KUNDEN):

    first = random.choice(first_names)
    last = random.choice(last_names)
    city, country = rand_city()

    values.append(
        f"""('{last} Handels GmbH','{first} {last}','Purchasing','{rand_street()}',
'{city}','{city}','{rand_plz()}','{country}','{rand_phone()}','{rand_phone()}')"""
    )

print("TRUNCATE TABLE oltp.Kunde;")
print("""INSERT INTO oltp.Kunde
(firma,kontakt,position,strasse,ort,region,plz,land,telefon,telefax)
VALUES""")
print(",\n".join(values) + ";\n")

# Artikel
values = []
for i in range(NUM_ARTIKEL):

    name = f"{random.choice(product_prefix)} Product {i+1}"

    values.append(
        f"({random.randint(1, NUM_LIEFERANTEN)},{random.randint(1, NUM_KATEGORIEN)},'{name}','pcs',{rand_price()},{random.randint(10, 500)},10,0)"
    )

print("TRUNCATE TABLE oltp.Artikel;")
print("""INSERT INTO oltp.Artikel
(liefer_nr,kat_nr,name,liefer_einheiten,einz_preis,lagerbestand,min_bestand,auslauf_art)
VALUES""")
print(",\n".join(values) + ";\n")

# Bestellungen
values = []
for _ in range(NUM_BESTELLUNGEN):

    city, country = rand_city()

    days = random.randint(50, 36*30)
    versand = datetime.now() - timedelta(days=days)

    bestell = versand - timedelta(days=random.randint(1, 10))
    liefer = versand + timedelta(days=random.randint(1, 10))

    values.append(
        f"""({random.randint(1, NUM_KUNDEN)},
{random.randint(1, NUM_PERSONAL)},
'{random.choice(first_names)} {random.choice(last_names)}',
'{rand_street()}','{city}','{city}','{rand_plz()}','{country}',
{random.randint(1, NUM_FIRMEN)},
'{bestell.strftime("%Y-%m-%d")}','{liefer.strftime("%Y-%m-%d")}','{versand.strftime("%Y-%m-%d")}',
{rand_price()},
{random.randint(1, NUM_FIRMEN)})""".replace("\n", "")
    )

print("TRUNCATE TABLE oltp.Bestellung;")
print("""INSERT INTO oltp.Bestellung
(kunden_code,personal_nr,empfaenger,strasse,ort,region,plz,ziel_land,versand_firma,
bestelldatum,lieferdatum,versanddatum,frachtkosten,firma_nr)
VALUES""")
print(",\n".join(values) + ";\n")

# Bestellartikel
values = []
for _ in range(NUM_DETAILS):

    values.append(
        f"""({random.randint(1, NUM_BESTELLUNGEN)},
{random.randint(1, NUM_ARTIKEL)},
{rand_price()},
{random.randint(1, 10)},
{round(random.choice([0, 0, 0, 0, 0, 0, 0.10, 0.15, 0.20]), 2)})""".replace("\n", "")
    )

print("TRUNCATE TABLE oltp.BestellArtikel;")
print("""INSERT INTO oltp.BestellArtikel
(bestell_nr,artikel_nr,einzelpreis,anzahl,rabatt)
VALUES""")
print(",\n".join(values) + ";")
