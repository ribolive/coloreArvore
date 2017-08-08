from Aresta import Aresta
from Vertice import Vertice

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
        self.listVertice = {}
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
            cor = None
            self.grafo[linha][self.qtdVertices] = cor
            self.listAresta.append(Aresta(a, b, cor))
            vA = Vertice(a)
            vB = Vertice(b)
            if a not in self.verticesChaves:
                self.listVertice[a] = vA
                self.verticesChaves.append(a)
            if b not in self.verticesChaves:
                self.listVertice[b] = vB
                self.verticesChaves.append(b)

            self.listVertice[a].insereVizinho(b, cor)  
            self.listVertice[b].insereVizinho(a, cor)

    def coloreAresta(self):
        qtdArestasLidas = 0
        elementos = {} 
        maxGrau = self.getMaxGrau()
        for i in range(self.qtdVertices):
            elementos[i] = set()
        while (qtdArestasLidas != self.qtdArestas):
            v1 = -1
            v2 = -1
            for i in range(self.qtdVertices):
                linha = qtdArestasLidas
                coluna = i
                if(self.grafo[linha][coluna] == 1 and v1 == -1):
                    v1 = coluna
                elif(self.grafo[linha][coluna] == 1):
                    v2 = coluna
                    break
            if not (( v1 == -1 ) or ( v2 == -1)):
                for i in range(maxGrau):
                    cor = i + 1  
                    if not ((cor in elementos[v1]) or (cor in elementos[v2])):
                        self.grafo[linha][self.qtdVertices] = cor
                        elementos[v1].add(cor)
                        elementos[v2].add(cor)

                        self.listVertice[v1].setCorVizinho(v2, cor)
                        self.listVertice[v2].setCorVizinho(v1, cor)
                        break
            qtdArestasLidas += 1

    def imprimeArestas(self):
        for i in range(self.qtdArestas):
            msg = self.listAresta[i].getString()
            print(msg)

    def imprimeGrafo(self):
        for i in range(self.qtdArestas):
            print (*self.grafo[i])

    def atualizaArestas(self):
        vizinhos = []
        self.listAresta.clear()
        for i in range(self.qtdArestas):
            for j in range (self.qtdVertices):
                if self.grafo[i][j] == 1:
                    vizinhos.append(j)
            v1 = vizinhos[0]
            v2 = vizinhos[1]
            cor = self.grafo[i][self.qtdVertices]
            # print (v1, v2, cor)
            self.listAresta.append(Aresta(v1, v2, cor))
            vizinhos.clear()
           

    def exportarGrafo(self):
        self.atualizaArestas()
        arquivo = open(self.nomeAqrSaida, "w")
        arquivo.write("graph G {\n")

        for i in range(self.qtdArestas):
            msg = self.listAresta[i].getString()
            arquivo.write(msg + "\n")

        arquivo.write('}')
        arquivo.close()
        # para criar grafo visual (instalar Graphiviz)
        # os.system('dot -Tpng saida.txt -o saida.png')

    def getMaxGrau(self):
        maiorGrau = 0
        for chave in self.listVertice:
            grauAtual = self.listVertice[chave].getGrau() 
            if(grauAtual > maiorGrau):
                maiorGrau = grauAtual
        return maiorGrau

    def imprimeVertices(self):
        for chave in self.listVertice:
            self.listVertice[chave].imprime();