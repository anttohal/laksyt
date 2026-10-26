class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}, sivumäärä: {self.sivumaara}")

# Aliluokka "Lehti"
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")

julkaisu1 = Lehti("Aku Ankka", "Aki Hyyppä")
julkaisu2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

julkaisu1.tulosta_tiedot()
print()
julkaisu2.tulosta_tiedot()