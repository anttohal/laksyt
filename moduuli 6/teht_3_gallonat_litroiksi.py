
def muunnos(gallonat : float):
    return gallonat * 3.785

annetut_gallonat = float(input('Anna gallona(t): '))

while annetut_gallonat >= 0:
    litrat = muunnos(float(annetut_gallonat))
    print(f"Gallona(t) litorina: {litrat:.2f} l")
    annetut_gallonat = float(input('Anna gallona(t): '))
