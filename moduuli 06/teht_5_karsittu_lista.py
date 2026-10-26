# Listan karsinta uuteen listaan ja sen palautus
def listan_karsinta(annettu_lista: list[int]):
    uusi_lista = []
    for num in annettu_lista:
        if num % 2 == 0:
            uusi_lista.append(num)
    return uusi_lista

lista = [1,2,3,4,5,6,7]

# Listojen tulostus
print(f"Alkuperäinen: {lista}")
print(f"Karsittu: {listan_karsinta(lista)}")