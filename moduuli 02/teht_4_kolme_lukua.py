# Luetaan syötteet
luku1 = int(input('Anna 1. luku: '))
luku2 = int(input('Anna 2. luku: '))
luku3 = int(input('Anna 3. luku: '))

# Laskutoimitukset
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa // 3

# Tulostetaan tulokset
print(f"Summa on {summa}")
print(f"Tulo on {tulo}")
print(f"Keskiarvo on {keskiarvo}")