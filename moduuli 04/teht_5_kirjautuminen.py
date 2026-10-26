# Haulutut arvot
haluttu_tunnus = "python"
haluttu_salasana = "rules"
kirjautumis_yritykset = 0

# Pyydä tunnus ja salasana
# Tulostaa vastauksen kirjautumisyrityksiin
while kirjautumis_yritykset < 5:
    tunnus = input('Anna tunnus: ')
    salasana = input('Anna salasana: ')
    if tunnus == haluttu_tunnus and salasana == haluttu_salasana:
        print("Tervetuloa")
        break
    kirjautumis_yritykset += 1
else:
    print("Pääsy evätty")