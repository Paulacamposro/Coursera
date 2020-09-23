def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista) - 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio] == elemento:
            print(meio)
            return meio
        elif elemento < lista[meio]:
            ultimo = meio - 1
        elif elemento > meio:
            primeiro = meio + 1
        print(lista[meio-1])
    return False 
