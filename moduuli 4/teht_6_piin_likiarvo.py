import random

# Muuttujat
maara = int(input('Anna määrä: '))
maara_ympyrassa = 0
kerrat = 0

while kerrat < maara:
    # Koordanaatit väliltä (-1, 1)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Laskutoimitukset
    if pow(x, 2) + pow(y, 2) < 1:
        maara_ympyrassa += 1
    kerrat += 1

# Laskee ja tulostaa likiarvon
print(f"Pii: {4 * maara_ympyrassa / maara}")