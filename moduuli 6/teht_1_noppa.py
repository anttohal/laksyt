import random

def noppa():
    silmaluku = random.randint(1,6)
    return silmaluku

luku = 0
while luku != 6:
    luku = noppa()
    print(luku)
