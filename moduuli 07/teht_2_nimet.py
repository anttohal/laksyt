# Nimijoukko
nimet = set()

# Kysy nimiä ja lisää ne joukkoon, kunnes annetaan tyhjä merkkijono

nimi = input('Anna nimi: ')
while nimi != "":
    # Tulostetaan onko nimi joukossa
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimet.add(nimi)
    nimi = input('Anna nimi: ')

# Tulosta nimet joukosta
print()
for annettu_nimi in nimet:
    print(annettu_nimi)