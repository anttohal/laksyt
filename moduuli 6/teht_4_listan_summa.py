def summaus(lista: list[int]):
    summa = 0
    for num in lista:
        summa += num
    return summa

lista = [22,45,76,49,11,46,2,21,3,41,14,55,70,9]
print(f"Listan summa: {summaus(lista)}")
