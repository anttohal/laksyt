minimi_pituus = 37
pituus = float(input('Anna pituus: '))

if pituus < minimi_pituus:
    print(f"Laske kalav takaisin! Se on {minimi_pituus - pituus:.2f} senttiä liian lyhyt.")