class Auto:
    def __init__(self, rekisteritunnus, huippunopeus : float):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeus):
        self.nykynopeus = min(self.huippunopeus, max(0, self.nykynopeus + nopeus))
        return

auto = Auto("ABC-123", 142)

print("Auton tiedot")
print(f"Tunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nopeus nyt: {auto.nykynopeus} km/h")
print(f"Matka: {auto.kuljettu_matka} km")

print()
auto.kiihdyta(70)
print(f"Auton {auto.rekisteritunnus} nopeus tällä hetkellä on {auto.nykynopeus} km/h")
auto.kiihdyta(50)
print(f"Auton {auto.rekisteritunnus} nopeus tällä hetkellä on {auto.nykynopeus} km/h")
auto.kiihdyta(-200)
print(f"Auton {auto.rekisteritunnus} nopeus tällä hetkellä on {auto.nykynopeus} km/h")