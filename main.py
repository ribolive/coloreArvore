from Grafo import Grafo
import sys

def main():
    if len(sys.argv) == 1:
        nomeGrafoEntrada = "grafo.txt"
        nomeGrafoSaida = "saida.txt"
    else:
        nomeGrafoEntrada = sys.argv[1]
        nomeGrafoSaida = sys.argv[2]
    grafo = Grafo(nomeGrafoEntrada, nomeGrafoSaida)

    # print(" ----  IMPRIME GRAFO ---- ")
    # grafo.imprimeGrafo()
    print(" + --------------------------------------------- +")
    print("  > Arquivo de entrada: ", nomeGrafoEntrada)
    print("\n  > Colorindo Arestas...")
    grafo.coloreAresta()
    print()
    # print(" ----  IMPRIME GRAFO ---- ")
    # grafo.imprimeGrafo()

    # print(" ---- IMPRIME VERTICES ---- ")
    # grafo.imprimeVertices()

    # print(" ---- ATUALIZA E IMPRIME ARESTA ---- ")
    # grafo.imprimeArestas()
    # grafo.imprimeArestas()

    print("  > Exportando... Arquivo de saída: ", nomeGrafoSaida)
    grafo.exportarGrafo()
    print(" + --------------------------------------------- +")
if __name__ == '__main__':
    main()
