# Tallennetut vuodenajat
vuodenajat = ("kevät", "kesä", "syksy", "talvi")

# Kysytään kuukautta
kuukausi = int(input('Anna kuukausi: '))

# Indeksin haku kuukaudesta
def hae_indeksi_kuuaudesta(kuukausi : int):
    # Yhtälössä (kuukausi - kuukausi % 3)
    #
    # Lopuksi tulos vähennetään 3 kääntäen indeksihaun 3...0 hakuun 0...3
    return 3 - (kuukausi - kuukausi % 3) % 4

# Vuodenajan haku
indeksi = hae_indeksi_kuuaudesta(kuukausi)
vuodenaika = vuodenajat[indeksi]

print(f"Kuukauden {kuukausi} vuodenaika on {vuodenaika}")