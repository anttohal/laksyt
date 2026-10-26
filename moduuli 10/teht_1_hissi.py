class Hissi:
    def __init__(self, alin_kerros : int, ylin_kerros : int):
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
        print(f"Hissi on {self.nyky_kerros}. kerroksessa.")
        return

    def kerros_alas(self):
        self.nyky_kerros -= 1
        print(f"Hissi on {self.nyky_kerros}. kerroksessa.")
        return

h = Hissi(1, 8)

h.siirry_kerrokseen(5)
print()
h.siirry_kerrokseen(h.alin_kerros)