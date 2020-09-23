''' O método especial __init__ , conhecido como método construtor da classe
é chamado automaticamente pelo inerpretador quando os objetos são criados
(quando as classes são instanciadas)'''

def main():
    carro1 = Carro('brasilia', 1968, 'amarela', 80)
    carro2 = Carro('fuscão', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, velomax):
        self.model = modelo
        self.an = ano
        self.co = cor
        self.vel = 0
        self.vmax = velomax

    def imprima(self):
        if self.vel == 0:
            print("%s %s %d"%(self.model, self.co, self.an))
        elif self.vel < self.vmax:
            print("%s %s indo a %d km/h"%(self.model, self.co, self.vel))
        else:
            print("%s %s indo muiiiiito rápido!!!"%(self.model, self.co))

    def acelere(self, veloc): 
        self.vel = veloc
        if self.vel > self.vmax:
            self.vel = self.vmax
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

main()
