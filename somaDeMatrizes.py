def soma_matrizes(m1, m2):
    matriz_soma = []
    linha = len(m1)
    coluna = len(m1[0])
    linha2 = len(m2)
    coluna2 = len(m2[0])
    if linha == linha2 and coluna == coluna2:
        for i in range(linha):
            matriz_soma.append([])
            for j in range(coluna):
                soma = m1[i][j] + m2[i][j]
                matriz_soma[i].append(soma)
        return matriz_soma

    else:
        return False
    
