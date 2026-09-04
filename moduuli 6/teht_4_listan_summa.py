def summaus(annettu_lista: list[int]):
    summa = 0
    for num in annettu_lista:
        summa += num
    return summa

lista = [1,2,3,4,5]
print(f"Listan summa: {summaus(lista)}")
