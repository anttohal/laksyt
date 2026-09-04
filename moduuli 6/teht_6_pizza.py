from math import pi

def yksikkohinta(halkaisija: float, eurot : float):
    ala = 2 * pi * (halkaisija * 0.5)
    return ala / (eurot * 100)

def pizzanhinta():
    pizza_halkaisija = float(input("Anna halkaisija (cm): "))
    pizza_hinta = float(input("Anna hinta (€): "))
    return yksikkohinta(pizza_halkaisija, pizza_hinta)

pizza_1 = pizzanhinta()
pizza_2 = pizzanhinta()

print("")
if pizza_1 < pizza_2:
    print("Pizza 1:n hinta suhde on parempi!")
else:
    print("Pizza 2:n hinta suhde on parempi!")
print("")
print(f"Pizza 1: {pizza_1:.2f}€")
print(f"Pizza 2: {pizza_2:.2f}€")