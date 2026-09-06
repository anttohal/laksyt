# Kysytään lentokentän ICAO-koodi ja tulostetaanse, jos se on tallennettu
def kentan_haku():
    kenttakoodi = input('Anna kentan koodi: ')
    if not kenttakoodi in lentokentat.keys():
        print(f"Koodia ei löydy: {kenttakoodi}")
        return
    else:
        print(f"{kenttakoodi}: {lentokentat[kenttakoodi]}")

# Kysytään ja tallennetaan lentokenttä ja sen ICAO-koodi
def kentan_syote():
    kentta = input('Anna kentta: ')
    koodi = input('Anna koodi: ')
    lentokentat[koodi.upper()] = kentta

lentokentat = {}

syote = input('Mitä haluat: (S)yota, (H)ae, (L)opeta: ').lower()

# Pääohjelma
while True:
    if syote == "s" or syote == "syota":
        kentan_syote()
    if syote == "h" or syote == "hae":
        kentan_haku()
    elif syote == "l" or syote == "lopeta":
        print("Näkemiin")
        break
    syote = input('Mitä haluat: (S)yota, (H)ae, (L)opeta: ')