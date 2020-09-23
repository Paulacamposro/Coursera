def menor_nome(nomes):
    min = nomes[0].strip(" ")
    tam = len(nomes[0].strip(" "))
    i = 1
    while i < len(nomes):
        if len(nomes[i].strip(" ")) < len(min):
            min = nomes[i].strip(" ")
        i = i + 1
    return min.capitalize()
