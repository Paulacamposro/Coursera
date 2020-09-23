def testa_minima():
    print("Iniciando testes")
    temps = []
    if testa_minima(temps) != 0:
        print("Valor errado para array", temps)
    temps = [0, 0, 0, 0, 0]
    if testa_minima(temps) != 0:
        print("Valor errado para array", temps)
    temps = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Finalizando testes")

def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array", temp)
        print("Valor esperado para array", valor_esperado, ". Valor calculado: ", valor_calculado)

def testa_minima(): # extrair linhas repetidas , fazer
    print("Iniciando testes")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual([30, 27, 26, 35, 22, 25, 23], 22)
    teste_pontual([-15, -12, 0, 20, 30], -15)
    print("Finalizando testes")
