MAIUSCULAS = [dec_code for dec_code in range(65, 91)]

def eh_caracter_maiusculo(caracter):
    letra = False
    for i in caracter:
        letra = letra or i.isupper()
    return ord(caracter) in MAIUSCULAS

def maiusculas(frase):
    i = 1
    while i < len(frase):
        acumulador = ''
        for caracter in frase:
            if eh_caracter_maiusculo(caracter):
                acumulador = acumulador + caracter
        return acumulador
