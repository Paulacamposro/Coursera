num = int(input("Digite um numero inteiro: "))

adj = False
resto = num % 10
num = num // 10

while num > 0 and not adj:
    restoatual = num % 10
    num = num // 10
    if restoatual == resto:
        adj = True
    resto = restoatual

if adj:
    print("sim")
else:
    print("não")
