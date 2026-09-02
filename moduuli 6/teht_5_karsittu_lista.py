def listan_karsinta(annettu_lista: list[int]):
    lista = []
    for num in annettu_lista:
        if num % 2 == 0:
            lista.append(num)
    return lista
#
lista = [221,45,76,49,11,46,2,21,3,41,14,55,707,9]
print(f"Alkuperäinen: {lista}")
print(f"Karsittu: {listan_karsinta(lista)}")