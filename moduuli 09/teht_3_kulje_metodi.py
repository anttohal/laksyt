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