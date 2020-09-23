def eh_primo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x / 2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True


def n_primos(n):

    if (n < 2):
        return 0
    elif (n == 2):
        return 1
    else:
        contador = 1
        while (n > 2):
            if (eh_primo(n)):
                contador += 1
            n -= 1
        return contador

    return 0

n = int(input("Digite um numero inteiro >= 2: "))
