from Grafo import Graph
from Dijktra import shortest_path_lengths, shortest_path_three, format_path_to_three

grafo = Graph()

A = grafo.insert_vertex('A')
B = grafo.insert_vertex('B')
C = grafo.insert_vertex('C')
D = grafo.insert_vertex('D')
E = grafo.insert_vertex('E')
F = grafo.insert_vertex('F')
G = grafo.insert_vertex('G')
 
grafo.insert_edge(A, B,10)
grafo.insert_edge(A, C,15)
grafo.insert_edge(B, D, 4)
grafo.insert_edge(B, C, 9)
grafo.insert_edge(D, E, 1)
grafo.insert_edge(E, F, 2)
grafo.insert_edge(F, G, 1)
grafo.insert_edge(G, A, 1)


cloud = shortest_path_lengths(grafo, B)
tree = shortest_path_three(grafo, B, cloud)
f_three = format_path_to_three(grafo, B, tree, A)

for i in f_three:
    print(i)
print('Coste del viaje', cloud[A])