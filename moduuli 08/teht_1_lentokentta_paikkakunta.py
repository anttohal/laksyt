import mysql.connector

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
koodi = input("Anna ICAO-koodi: ")
sql = f"select name, municipality from airport where ident = '{koodi}'"
kursori = yhteys.cursor()
kursori.execute(sql)

# Haetaan ja käsitellään tulokset
tulos = kursori.fetchall()[0]
print(f"\nKenttä: {tulos[0]}\nPaikkakunta: {tulos[1]}")
