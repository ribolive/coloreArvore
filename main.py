from Grafo import Grafo

def main():
    grafo = Grafo("grafo.txt", "saida.txt")
    grafo.imprimeAresta()
    grafo.exportarGrafo()
    grafo.imprimeGrafo()

if __name__ == '__main__':
    main()
