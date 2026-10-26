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
sql = f"select type, count(type) from airport where iso_country = '{koodi}' group by type"
kursori = yhteys.cursor()
kursori.execute(sql)

# Haetaan ja käsitellään tulokset
tulos = kursori.fetchall()
print(f"\nMaan ({koodi}) kenttätyypit/määrät:")
print()
for osa in tulos:
    print(f"{osa[0]}: {osa[1]}")
