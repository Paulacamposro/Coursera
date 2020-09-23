def ordenada(lista):
    menor = lista[0]
    i = 1
    crescente = True
    while i < len(lista) and crescente:
        if lista[i] < menor:
            crescente = False
        menor = lista[i]
        i = i + 1
    if crescente:
        return True
    else:
        return False             
