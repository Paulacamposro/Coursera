def remove_repetidos(lista):
    novalista = []
    for i in lista:
        if i not in novalista:
            novalista.append(i)
    novalista.sort()
    return novalista

lista = [3, 7, 9, 15, 21, 27, 18, 12, 6, 15, 3, 3, 21]

lista = remove_repetidos(lista)
print (lista)
