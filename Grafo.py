from Aresta import Aresta

import os 
class Grafo(object):
    def __init__(self, nomeAqrEntrada, nomeAqrSaida): 
        self.nomeAqrSaida = nomeAqrSaida
        self.nomeAqrEntrada = nomeAqrEntrada
        self.arquivo = open(self.nomeAqrEntrada, "r")
        self.linhasAqr = self.arquivo.read().splitlines()
        self.qtdVertices = int(self.linhasAqr[1])
        self.qtdArestas = (len(self.linhasAqr) - 3)
        self.verticesChaves = []
        self.listAresta = []
        self.grafo = None
        self.__constroiGrafo()

    def __constroiGrafo(self):
       # construindo o grafo Matriz de Incidencia (MxN)
        self.grafo = [[0 for i in range(self.qtdVertices + 1)] for i in range(self.qtdArestas)]

        for i in range(2, len(self.linhasAqr) -1):
            linha = i - 2
            # print(self.linhasAqr[i])
            a,b = map(int,self.linhasAqr[i].split("--"))
            self.grafo[linha][a] = 1
            self.grafo[linha][b] = 1
            self.grafo[linha][self.qtdVertices] = None
            self.listAresta.append(Aresta(a,b))
            if a not in self.verticesChaves:
                self.verticesChaves.append(a)
            if b not in self.verticesChaves:
                self.verticesChaves.append(b)

    # def coloreAresta(self):
    #     qtdArestasLidas = 0
    #     elementos = {}
    #     for i in range(self.qtdVertices):
    #         elementos[i] = set()
    #     while (qtdArestasLidas != self.qtdArestas):
    #         v1 = -1
    #         v2 = -1
    #         for i in range(self.qtdVertices - 1):
    #             linha = qtdArestasLidas
    #             coluna = i
    #             if(grafo[linha][coluna] == 1 && v1 == -1):
    #                 v1 = coluna
    #             elif(grafo[linha][coluna] == 1):
    #                 v2 = coluna
    #                 break
    #         for i in range(1,6): # TROCAR O 5 POR GRAU MAX
    #             if not ((i in elementos[v1]) or (i in elementos[v2])):
    #                 grafo[linha][qtdVertices] = i
    #                 elementos[v1].add(i)
    #                 elementos[v2].add(i)
    #                 break
    #         qtdArestasLidas += 1

    def imprimeAresta(self):
        for i in range(self.qtdArestas):
            msg = self.listAresta[i].getString()
            print(msg)

    def imprimeGrafo(self):
        for i in range(self.qtdArestas):
            print (*self.grafo[i])

    def exportarGrafo(self):
        arquivo = open(self.nomeAqrSaida, "w")
        arquivo.write("graph G {\n")

        for i in range(self.qtdArestas):
            msg = self.listAresta[i].getString()
            arquivo.write(msg + "\n")

        arquivo.write('}')
        arquivo.close()
        os.system('dot -Tgif saida.txt -o saida.gif')