from random import randrange

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus : float):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeus):
        self.nykynopeus = min(self.huippunopeus, max(0, self.nykynopeus + nopeus))
        return

    def kulje(self, aika : float):
        self.kuljettu_matka += int(self.nykynopeus * aika)
        return

class Kilpailu:
    def __init__(self, nimi, pituus : float, auto_lista):
        self.nimi = nimi
        self.pituus = pituus
        self.auto_lista = auto_lista

    def tunti_kuluu(self, auto : Auto, tunnit : float):
        auto.kiihdyta(randrange(-10, 15))
        auto.kulje(tunnit)
        return

    def tulosta_tilanne(self):
        print(f"--== {self.nimi} Autojen Tiedot ==--")
        for auto in self.auto_lista:
            print(f"Auton tunnus: {auto.rekisteritunnus}  Huippunopeus: {auto.huippunopeus} km/h  Kuljettu matka: {auto.kuljettu_matka} km")
        return

    def kilpailu_ohi(self, auto : Auto):
        return auto.kuljettu_matka >= self.pituus



autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i+1}", randrange(100, 200)))

tunnit = 0
peli_paattyi = False

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

print(f"{kilpailu.nimi}")
print(f"Autoja ajetaan, kunnes jokin niistä ajaa {kilpailu.pituus} km")
print()
print("Paikoillanne... valmiit... Ajakaa!")
while not peli_paattyi:
    for auto in autot:
        kilpailu.tunti_kuluu(auto, tunnit)
        if kilpailu.kilpailu_ohi(auto):
            print()
            print(f"Peli ohi! Jokin autoista on ylittänyt {kilpailu.pituus} km rajan")
            peli_paattyi = True
            break
    tunnit += 1
    if tunnit % 10 == 0:
        print()
        print(f"Tunteja kulunut: {tunnit}")
        print()
        kilpailu.tulosta_tilanne()

print()
kilpailu.tulosta_tilanne()
