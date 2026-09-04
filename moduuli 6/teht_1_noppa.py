import random

# Silmäluvun arpominen
def noppa():
    silmaluku = random.randint(1,6)
    return silmaluku

luku = 0

# Silmäluvun etsintä ja tulostus
while luku != 6:
    luku = noppa()
    print(luku)
