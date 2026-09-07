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
koodi = input("Anna maakoodi: ")
sql = f"select count(name) from airport where iso_country = '{koodi}'"
kursori = yhteys.cursor()
kursori.execute(sql)

# Haetaan ja käsitellään tulokset
tulos = kursori.fetchall()[0]
print(f"\nMaan ({koodi}) kenttien määrä: {tulos[0]}")
