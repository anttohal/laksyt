lista = []

# Kysyy viittä kaupunkia
for i in range(5):
    arvo = input('Anna kaupunki: ')
    lista.append(arvo)

# Tulostaa kaupungit
print("")
for i in lista:
    print(f"{i}")