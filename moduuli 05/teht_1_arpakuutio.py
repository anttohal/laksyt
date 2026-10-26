import random

# Muuttujat
summa = 0
heitot = int(input('Anna heittomäärä: '))

# Heittää noppaa annettu määrä
# ja laskee heittojen summan
for i in range(heitot):
    heitto = random.randint(1, 6)
    summa += heitto

# Tulostaa summan
print(f"Heittojen summa: {summa}")