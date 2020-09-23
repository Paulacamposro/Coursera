
def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)

def numPositivo(n):
    while n >= 0:
        n = int(input("Digite um numero inteiro: "))
        fatorial(n)
