from AdaptableHeapPriorityQueue import AdaptableHeapPriorityQueue

def shortest_path_lengths(g,src):

    d = {}
    cloud = {}
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqlocator[v] = pq.add(d[v], v)
    
    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key
        del pqlocator[u]
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt
                    pq.update(pqlocator[v], d[v], v)
    
    return cloud

def shortest_path_three(g, s, d):

    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident_edges(v):
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] + wgt:
                    tree[v] = e
               
    
    return tree
    
def format_path_to_three(g,s,d, to):

    edge = d[to]
    next_v = edge.opposite(to)
    three = [edge]
    while not s in edge.endpoints():
        three.append(d[next_v])
        edge = d[next_v]
        next_v = edge.opposite(next_v)
    return reversed(three)