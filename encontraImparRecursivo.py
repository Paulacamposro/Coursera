def encontra_impares(lista):
    listaimp = []
    if len(lista) > 0:
        numero = lista.pop(0)
        if numero % 2 != 0:
            listaimp.extend([numero])
        listaimp = listaimp + encontra_impares(lista)
    return listaimp



    
