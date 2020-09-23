meuCartao = int(input("Digite o numero do cartão de credito: "))

cartaoLido = 1
encontrei = False

while cartaoLido != 0 and not encontrei:
    cartaoLido = int(input("Digite o numero do proximo cartao de credito:"))
    if cartaoLido == meuCartao:
        encontrei = True
if encontrei:
    print("Oba")
else:
    print("Xiii")
