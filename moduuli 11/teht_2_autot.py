class Auto:
    def __init__(self, rekisteritunnus, huippunopeus: float):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeus):
        self.nykynopeus = min(self.huippunopeus, max(0, self.nykynopeus + nopeus))
        return

    def kulje(self, aika: float):
        self.kuljettu_matka += int(self.nykynopeus * aika)
        return


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus : float, akkukapasiteetti : float):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta_lukemat(self):
        print(f"Tunnus: {self.rekisteritunnus}, Nopeus: {self.nykynopeus} km/h, Matka: {self.kuljettu_matka} km")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus : float, litrat: float):
        self.litrat = litrat
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta_lukemat(self):
        print(f"Tunnus: {self.rekisteritunnus}, Nopeus: {self.nykynopeus} km/h, Matka: {self.kuljettu_matka} km")

auto1 = Sahkoauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)

auto1.kiihdyta(35)
auto1.kulje(3)

auto2.kiihdyta(40)
auto2.kulje(3)

auto1.tulosta_lukemat()
print()
auto2.tulosta_lukemat()
