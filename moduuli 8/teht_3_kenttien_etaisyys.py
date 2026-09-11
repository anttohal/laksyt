import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='lentopeli',
    user='kayttaja1',
    password='Munpiha',
    autocommit=True,
    collation='utf8mb4_general_ci'
    )

# Kyselyn määrittely ja suoritus
koodi1 = input("Anna ICAO-koodi: ")
koodi2 = input("Anna ICAO-koodi: ")
sql = f"select name, latitude_deg, longitude_deg from airport where ident = '{koodi1}' or ident = '{koodi2}'"
kursori = yhteys.cursor()
kursori.execute(sql)

# Haetaan ja käsitellään tulokset
tulos = kursori.fetchall()
kentta1 = tulos[0]
kentta2 = tulos[1]
sijainti1 = kentta1[1:]
sijainti2 = kentta2[1:]
print(f"\nKenttien {kentta1[0]} ja {kentta2[0]} etäisyys on noin {geodesic(sijainti1, sijainti2).km:.2f} km")
