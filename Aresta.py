class Aresta(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.cor = -1

    def getV1(self):
        return self.v1

    def getV2(self):
        return self.v2

    def setCor(self, valor):
        self.cor = valor

    def getString(self):
        aresta = str(self.v1) + " -- " + str(self.v2)
        if(self.cor != -1):
            aresta += " [ label =" + str(self.cor) +" ]"
        return aresta
