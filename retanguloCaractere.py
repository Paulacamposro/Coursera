a = int(input("Digite a largura: "))
b = int(input("Digite a altura: "))
linha = 1
coluna = 1
caractere = "#"

while linha <= b:
    while coluna <= a:
        print(caractere,end = "")
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1
