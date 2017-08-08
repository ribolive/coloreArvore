class Vertice(object):
    def __init__(self, nome):
        self.nome = nome
        self.grau = 0
        self.vizinhos = []

    def getV1(self):
        return self.v1

    def insereVizinho(self, novoVizinho):
        self.vizinhos.append(novoVizinho)
        self.grau += 1