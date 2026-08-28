lista = []

# Kysyy arvoja
arvo = input('Anna luku tai lopeta painamalla Enter: ')
while arvo != "":
    lista.append(int(arvo))
    arvo = input('Anna luku tai lopeta painamalla Enter: ')

# Järjestää listan suurimmasta alkaen
lista.sort(reverse=True)

# Tulostaa listan
print("")
print(lista[0:5])
