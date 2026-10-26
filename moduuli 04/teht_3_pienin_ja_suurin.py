# Muuttujat
pienin = 0.0
suurin = 0.0

# Kysytään lukuja ja lisätään ne muuttujiin
luku = input('Anna luku: ')
while luku != "":
    if float(luku) < pienin:
        pienin = float(luku)
    elif float(luku) > suurin:
        suurin = float(luku)
    luku = input('Anna luku: ')

print("")

# Tulostetaan Luvut
print(f"Pienin luku: {pienin:.2f}")
print(f"Suurin luku: {suurin:.2f}")
