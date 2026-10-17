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

autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i+1}", randrange(100, 200)))

tunnit = 0
peli_paattyi = False

print("Auto-peli")
print("Autoja ajetaan, kunnes jokin niistä ajaa 10000 km")
print()
print("Paikoillanne... valmiit... Ajakaa!")
while not peli_paattyi:
    for auto in autot:
        auto.kiihdyta(randrange(-10, 15))
        auto.kulje(tunnit)
        if auto.kuljettu_matka >= 10000:
            print("Peli ohi! Jokin autoista on ylittänyt 10000 km rajan")
            peli_paattyi = True
            break
    tunnit += 1

print()
print("Autojen tiedot:")
print()
for auto in autot:
    print(f"Auton tunnus: {auto.rekisteritunnus}  Huippunopeus: {auto.huippunopeus} km/h  Kuljettu matka: {auto.kuljettu_matka} km")

