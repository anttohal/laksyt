from math import pi

# Yksikköhinnan lasku
def yksikkohinta(halkaisija: float, eurot : float):
    halkaisija = halkaisija / 100
    sade = halkaisija / 2
    ala = pi * sade * sade
    return ala / eurot

# Pizzan arvojen kysyntä ja yksikköhinnan lasku
def pizzanhinta():
    pizza_halkaisija = float(input("Anna halkaisija (cm): "))
    pizza_hinta = float(input("Anna hinta (€): "))
    return yksikkohinta(pizza_halkaisija, pizza_hinta)

# Pizzojen arvojen kysyntä
pizza_1 = pizzanhinta()
pizza_2 = pizzanhinta()


# Pizzojen hintojen vertailu ja tulostus
print("")
if pizza_1 < pizza_2:
    print("Pizza 1:n hinta suhde on parempi!")
else:
    print("Pizza 2:n hinta suhde on parempi!")
print("")
print(f"Pizza #1 yksikköhinta: {pizza_1:.2f}€")
print(f"Pizza #2 yksikköhinta: {pizza_2:.2f}€")