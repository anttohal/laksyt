# Kysyy lukua
luku = int(input('Anna luku: '))

# Tarkistaa, onko luku alkuluku
on_alkuluku = True
for i in range(2, int(pow(luku, 0.5)) + 1):
    if (luku <= 0) or (luku % i == 0):
        on_alkuluku = False
        break

# Tulostaa vastauksen
if on_alkuluku:
    print(f"Luku {luku} on alkuluku")
else:
    print(f"Luku {luku} ei ole alkuluku")

