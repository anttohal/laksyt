# Luetaan suorakulmion kanta ja korkeus
kanta = float(input('Anna suorakulmion kannan pituus: '))
korkeus = float(input('Anna suorakulmion korkeus: '))

# Laskutoimitukset
ala = kanta * korkeus
piiri = (kanta * 2) + (korkeus * 2)

# Tulostus
print(f"Suorakulmion pinta-ala on {ala:.2f}")
print(f"Suorakulmion piiri on {piiri:.2f}")