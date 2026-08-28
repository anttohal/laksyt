from random import randint

# Arvattava muuttuja
arvattava_luku = randint(1,10)

# Kysytään lukua ja tulostetaan vastaus arvaukseen
luku = int(input('Anna luku: '))
while luku != arvattava_luku:
    if luku < arvattava_luku:
        print("Liian pieni arvaus")
    if luku > arvattava_luku:
        print("Liian suuri arvaus")
    luku = int(input('Anna luku: '))
print("")
print("Oikein!")