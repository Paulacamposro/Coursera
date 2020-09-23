def maior_elemento(lista):
    for i in lista:
        novalista = list(set(lista))
    return novalista[-1]
