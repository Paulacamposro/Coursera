'''Escreva uma função que recebe um array de strings como parâmetro e devolve o
primeiro string na ordem lexicográfica, ignorando-se letras maiúsculas e minúsculas.'''

def ordem_lexo(lista):
    primeiro_lexo = lista[0].lower()
    i = 1
    while i < len(lista):
        if lista[i].lower() < primeiro_lexo:
            primeiro_lexo = lista[i].lower()
        i = i + 1
    return primeiro_lexo


def testa_menor_string():
    teste_pontual(["ana", "maria","José", "Valdemar"], "ana")
    teste_pontual(["anabele", "maria","José", "Ada"], "Ada")
