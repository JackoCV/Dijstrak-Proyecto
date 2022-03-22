from dijkstar import *

nodos=["A","B","C","D","E","F","G"]

grafo =  Graph();
grafo.add_node("A",{"B":3,"F":8,"G":4})
grafo.add_node("B",{"A":3,"C":2,"D":13})
grafo.add_node("C",{"B":2,"D":3,"E":15})
grafo.add_node("D",{"B":13,"C":3,"E":1,"F":2})
grafo.add_node("E",{"C":15,"D":1,"F":4})
grafo.add_node("F",{"A":8,"D":2,"E":4,"G":1})
grafo.add_node("G",{"A":4,"F":1})

opciones = ""
for i, nodo in enumerate(nodos):
    opciones += ("\n" + str(i + 1) + "-" + nodo)
while True:
    partida = int(input("Indique el inicio:\n" + opciones + "\n0-Salir\n"))
    if partida == 0: break
    destino = int(input("Indique el final:\n" + opciones + "\n0-Salir\n"))
    if destino == 0: break
    if partida == destino:
        print("Ya se encuentra en el lugar")
    else:
            camino = find_path(grafo, nodos[partida - 1], nodos[destino - 1])
            print("->".join(camino.nodes))
