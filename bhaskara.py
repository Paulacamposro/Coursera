import math

a = float(input("Digite o valor da constante a:"))
b = float(input("Digite o valor da constante b:"))
c = float(input("Digite o valor da constante c:"))

delta = (b**2)-(4*a*c)

if delta < 0:
    print("esta equação não possui raízes reais")

elif delta == 0:
    r = (-1*b)/(2*a)
    print("a raiz desta equação é",r)

elif delta > 0:
    x1 = ((-1*b) + math.sqrt(delta))/(2*a)
    x2 = ((-1*b) - math.sqrt(delta))/(2*a)
    if x1 < x2:
        print("as raízes da equação são",x1,"e",x2)
    else:
        print("as raízes da equação são",x2,"e",x1)
