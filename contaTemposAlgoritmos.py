''' Contatempos'''
import ordenador
import random
import time


class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000) # inteiros entrw 0 e 999
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenador.Ordenador()

        antes = time.time()
        o.bubblesort(lista1)
        depois = time.time()
        print("Bolha demorou", depois - antes)

        antes = time.time()
        o.selecao_direta(lista1)
        depois = time.time()
        print("Seleção direta demorou", depois - antes)
