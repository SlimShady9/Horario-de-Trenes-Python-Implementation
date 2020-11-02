class Vertex:
    __slots__ = '_element'

    def __init__(self, x):
        self._element = x

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))

    def __str__(self):
        return 'Vertice: ' + self.element()

class Edge:

    __slots__='_origin' , '_destination', '_element'

    def __init__(self, u , v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        return (self._origin, self._destination)

    def element(self):
        return self._element
    
    def opposite(self, v):
        return self._destination if v is self._origin else self._origin
    
    def __hash__(self):
        return hash((self._origin , self._destination))

    def __str__(self):
        ii,ij = self.endpoints()
        return 'Arista de ' + str(ii) + ' a ' + str(ij)


class Graph:
    # Implementacion de in grafo dirigido

    def __init__(self):

        self._outgoing = {}

    def vertex_count(self):

        return len(self._outgoing)
    
    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v] for v in self._outgoing))

        return total // 2
    
    def edges(self):
        result = set()
        for sec_map in self._outgoing.values():
            result.update(sec_map.values())
        return result
    
    def get_edge(self, u,v):
        return self._outgoing[u].get(v)

    def degree(self, v):

        adj = self._outgoing

        return len(adj[v])
    
    def incident_edges(self, v):

        adj = self._outgoing

        for edge in adj[v].values():
            yield edge
    
    def insert_vertex(self, x=None):
        v = Vertex(x)

        self._outgoing[v] = {}
        return v
    
    def insert_edge(self, u, v, x = None):
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._outgoing[v][u] = e




