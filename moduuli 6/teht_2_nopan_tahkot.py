import random

# Silmäluvun arpominen
def noppa(tahko : int):
    silmaluku = random.randint(1,tahko)
    return silmaluku

luku = 0
maksimi_luku = int(input('Anna maksimiluku: '))

# Silmäluvun etsintä ja tulostus
while luku != maksimi_luku:
    luku = noppa(maksimi_luku)
    print(luku)
