def eh_hipotenusa(i, j):
    return ((i * i) + (j * j))


def soma_hipotenusas(n):
    h = 1
    soma = 0
    while h <= n:
        hh = (h*h)
        i = 1
        j = 1
        while i < n:
            while j < n:
                if (hh == eh_hipotenusa(i, j)):
                    soma = soma + h
                    i = n
                    break
                j = j + 1
            i = i + 1
            j = i
        h = h + 1

    return soma


n = int(input("Digite um numero inteiro >= 2: "))
