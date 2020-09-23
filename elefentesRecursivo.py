def elefantes(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "Um elefante incomoda muita gente"
    elif n == 2:
        return elefantes(n-1) + f"\n{n} elefantes "+ incomodam(n) +"muito mais"
    else:
        frasepri = f"\n{n-1} elefantes incomodam muita gente"
        fraseseg = f"\n{n} elefantes "+ incomodam(n) +"muito mais"
        return elefantes(n-1) + frasepri + fraseseg

def incomodam(n):
    if n <= 0:
        return ""
    elif n == 1:
        return "incomodam "
    else:
        return "incomodam " + incomodam(n - 1)
