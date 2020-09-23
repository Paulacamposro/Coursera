def maiusculas(frase):
    letra = frase[0]
    i = 0

    while i < len(frase):
        if ord(frase[i]) >= 60 and ord(frase[i]) <=90:
            print(frase[i], end='')
        else:
            pass
        i = i + 1
