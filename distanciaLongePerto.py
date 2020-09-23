import math

x1 = int(input("Digite o primeiro número:"))
y1 = int(input("Digite o segundo número:"))
x2 = int(input("Digite o primeiro número do segundo ponto é:"))
y2 = int(input("Digite o segundo número do segundo ponto é:"))

d = ((x1 - x2)**2) + ((y1 - y2)**2)

if math.sqrt(d) >= 10:
    print("longe")
else:
    print("perto")
