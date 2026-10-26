# Tallennetut vuodenajat
vuodenajat = ("kevät", "kesä", "syksy", "talvi")

# Kysytään kuukautta
kuukausi = int(input('Anna kuukausi: '))

# Vuodenajan haku kuukaudesta
def hae_vuodenaika_kuukaudesta(kuukausi : int):
    # Yhtälöllä (kuukausi - kuukausi % 3) rajoitetaan haku 1 vuodenajan mittaiseksi (3 kk)
    # Tämän jälkeen etsitään, mille vuodenajalle yhtälön tulos osuu. Tämä saadaan
    # tuloksen ja 4:än jakojäännöksestä
    # Lopuksi joudutaan vielä vähentämään tulos 3:sta, näin kääntäen
    # indeksihaun laskevasta (3...0) nousevaan (0...3)
    return 3 - (kuukausi - kuukausi % 3) % 4

# Vuodenajan haku
indeksi = hae_vuodenaika_kuukaudesta(kuukausi)
vuodenaika = vuodenajat[indeksi]

print(f"Kuukauden {kuukausi} vuodenaika on {vuodenaika}")