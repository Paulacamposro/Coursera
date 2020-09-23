# verificar se um dado numero tem 2 numeros adjacentes iguais
num = int(input("Digite um numero: "))

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
    print("Este número tem adjacentes iguais.")
else:
    print("Este número não tem adjacentes iguais.")
