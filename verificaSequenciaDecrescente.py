descrescente = True
primeiro = int(input("Digite o primeiro número: "))

valor = 1

while valor != 0 and descrescente: 
    valor = int(input("Digite o próximo valor: "))
    if valor > primeiro:
        descrescente = False
    primeiro = valor
if descrescente:
    print("Esta sequencia é descrescente!")
else:
    print("Esta sequencia não é descrescente!")
