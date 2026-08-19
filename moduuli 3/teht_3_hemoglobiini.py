# Kysyy sukupuolta
sukupuoli = input('(M)ies vai (n)ainen? ')

# Kysyy hemoglobiiniarvoa
hemo_arvo = int(input('Anna hemoglobiiniarvo (g/l): '))

if sukupuoli == "nainen" or sukupuoli == "n":
    if hemo_arvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo_arvo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "mies" or sukupuoli == "m":
    if hemo_arvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo_arvo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
