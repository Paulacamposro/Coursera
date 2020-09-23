a = int(input("Digite a largura: "))
b = int(input("Digite a altura: "))
linha = 1
coluna = 1
caractere = "#"

while linha <= b:
    print(caractere * a, end = "")
    print()
    linha  = linha + 1
    while linha > 1 and linha < b:
        print(caractere + ' ' * (a - 2) + caractere)
        linha  = linha + 1
