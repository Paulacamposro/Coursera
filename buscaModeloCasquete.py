class Casquete:
    def __init__(self, titulo, marca, artista, ano):
        self.titulo = titulo
        self.marca = marca
        self.artista = artista
        self.ano = ano 

class Buscador:
    def busca_por_titulo(self, colecao, titulo):
        for i in range(len(colecao)):
            if colecao[i].titulo == titulo:
                return i
        return -1

    def vamos_buscar(self):
        colecao = [Casquete("Folhas pequenas", "MMe Ciseaux", "Paula Campos", 2015),
                   Casquete("Folhas grandes", "MMe Ciseaux", "Paula Campos", 2016),
                   Casquete("Metal", "MMe Ciseaux", "Paula Campos", 2017)]

        onde_achou = self.busca_por_titulo(colecao, "Metal")

        if onde_achou == -1:
            print("O casquete não está nessa coleção")
        else:
            preferida = colecao[onde_achou]
            print(preferida.titulo, preferida.marca, preferida.artista, preferida.ano, sep = ',');
