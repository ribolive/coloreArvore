class Vertice(object):
    def __init__(self, nome):
        self.nome = nome
        self.grau = 0
        self.vizinhos = {}

    def getV1(self):
        return self.v1

    def getGrau(self):
        return self.grau

    def insereVizinho(self, novoVizinho, cor):
        self.vizinhos[novoVizinho] = cor
        self.grau += 1

    def imprime(self):
        print("Nome: ", self.nome)
        print("Grau: ", self.grau)
        print("Vizinhos :", self.vizinhos)

    def setCorVizinho(self, chave, cor):
        self.vizinhos[chave] = cor