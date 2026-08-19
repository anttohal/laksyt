from math import floor

leiviskät = float(input('Anna leiviskät. \n'))
naulat = float(input('\nAnna naulat. \n'))
luodit = float(input('\nAnna luodit. \n'))

# Muunnokset
leiviskä_nauloiksi = leiviskät * 20.0
naula_luodeiksi = (naulat + leiviskä_nauloiksi) * 32.0
luodit_grammoiksi = (luodit + naula_luodeiksi) * 13.3

# Kilojen ja grammojen erotus
kilot = floor(luodit_grammoiksi * 0.001)
grammat = (luodit_grammoiksi * 0.001 - kilot) * 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {grammat:.2f} grammaa")