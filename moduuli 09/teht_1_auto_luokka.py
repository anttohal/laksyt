class Auto:
    def __init__(self, rekisteritunnus, huippunopeus : float):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", 142)

print("Auton tiedot")
print(f"Tunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nopeus nyt: {auto.nykynopeus} km/h")
print(f"Matka: {auto.kuljettu_matka} km")