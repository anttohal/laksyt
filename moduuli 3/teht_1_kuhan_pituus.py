# Kuhan minimipituus
minimi_pituus = 37

# Syötetään saadun kuhan pituus
pituus = float(input('Anna pituus: '))

# Tulostetaan jos pituus ei vastaa minimiä
if pituus < minimi_pituus:
    print(f"Laske kala takaisin! Se on {minimi_pituus - pituus:.2f} senttiä liian lyhyt.")