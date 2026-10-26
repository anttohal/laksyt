class Hissi:

    hissi_numero = 0

    def __init__(self, alin_kerros : int, ylin_kerros : int):
        Hissi.hissi_numero += 1
        self.hissi_numero = Hissi.hissi_numero
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nyky_kerros = self.alin_kerros

    def siirry_kerrokseen(self, kohdekerros : int):
        kohdekerros = min(self.ylin_kerros, max(self.alin_kerros, kohdekerros))
        while True:
            if self.nyky_kerros == kohdekerros:
                break
            if kohdekerros > self.nyky_kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()

    def kerros_ylos(self):
        self.nyky_kerros += 1
        print(f"Hissi #{self.hissi_numero} on {self.nyky_kerros}. kerroksessa.")
        return

    def kerros_alas(self):
        self.nyky_kerros -= 1
        print(f"Hissi #{self.hissi_numero} on {self.nyky_kerros}. kerroksessa.")
        return

class Talo:
    def __init__(self, alin_kerros : int, ylin_kerros : int, hissien_maara : int):
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, pyydetty_hissi : int, kohdekerros : int):
        h = self.hissit[pyydetty_hissi- 1]
        h.siirry_kerrokseen(kohdekerros)

t = Talo(1, 6, 4)

t.aja_hissia(1,4)
print()
t.aja_hissia(2, 6)
print()
t.aja_hissia(3,2)
print()
t.aja_hissia(4, 3)
