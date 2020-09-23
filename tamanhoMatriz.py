def minha_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            matriz[i][j] = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
        matriz.append(linha)

    return matriz

def dimensoes(matriz):
    tamanho = (len(matriz), len(matriz[0]))
    print('{}X{}'.format(tamanho[0], tamanho[1]))
