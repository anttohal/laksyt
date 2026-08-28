lista = []

# Kysyy arvoja
arvo = input('Anna luku tai lopeta painamalla Enter: ')
while arvo != "":
    lista.append(int(arvo))
    arvo = input('Anna luku tai lopeta painamalla Enter: ')

# Järjestää listan suurimmasta alkaen
lista.sort(reverse=True)

print("")

# Tulostaa listan
print(lista[0:min(len(lista), 5)])
