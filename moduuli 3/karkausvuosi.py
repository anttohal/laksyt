vuosi = int(input('Anna vuosi: '))

print(vuosi % 100)
print(vuosi % 400)
print(vuosi % 4)

if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        print(f"{vuosi} on karkausvuosi")
    else:
        print(f"{vuosi} ei ole karkausvuosi")
else:
    if vuosi % 4 == 0:
        print(f"{vuosi} on karkausvuosi")
    else:
        print(f"{vuosi} ei ole karkausvuosi")