tamanho = int(input("Digite o tamanho da sequencia: "))
anterior = int(input("Digite o numero: "))
i = 1
crescente = True

while i < tamanho:
    atual = int(input("Digite o proximo valor: "))
    if atual < anterior:
        crescente = False
    anterior = atual
    i = i + 1

if crescente:
    print("crescente")
else:
    print("descrescente")
