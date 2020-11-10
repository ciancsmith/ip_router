from pqdict import PQDict
import router as r

def dijkstra(G, start, end=None):
    '''
    dijkstra's algorithm determines the length from `start` to every other 
    vertex in the graph.
    The graph argument `G` should be a dict indexed by nodes.  The value 
    of each item `G[v]` should also a dict indexed by successor nodes.
    In other words, for any node `v`, `G[v]` is itself a dict, indexed 
    by the successors of `v`.  For any directed edge `v -> w`, `G[v][w]` 
    is the length of the edge from `v` to `w`.
        graph = {'a': {'b': 1}, 
                 'b': {'c': 2, 'b': 5}, 
                 'c': {'d': 1},
                 'd': {}}
    Returns two dicts, `dist` and `pred`:
        dist, pred = dijkstra(graph, start='a') 
    
    `dist` is a dict mapping each node to its shortest distance from the
    specified starting node:
        assert dist == {'a': 0, 'c': 3, 'b': 1, 'd': 4}
    `pred` is a dict mapping each node to its predecessor node on the
    shortest path from the specified starting node:
        assert pred == {'b': 'a', 'c': 'b', 'd': 'c'}
    
    '''
    inf = float('inf')
    D = {start: 0}          # mapping of nodes to their dist from start
    Q = PQDict(D)           # priority queue for tracking min shortest path
    P = {}                  # mapping of nodes to their direct predecessors
    U = set(G.router_list.keys())       # unexplored nodes

    while U:                                    # nodes yet to explore
        (v, d) = Q.popitem()                    # node w/ min dist d on frontier
        D[v] = d                                # est dijkstra greedy score
        U.remove(v)                # remove from unexplored
        if v == end: break

        # now consider the edges from v with an unexplored head -
        # we may need to update the dist of unexplored successors 
        for w in G.router_list[v]:                          # successors to v
            if w in U:                          # then w is a frontier node
                d = D[v] + G.router_list[v][w]              # dgs: dist of start -> v -> w
                if d < Q.get(w, inf):
                    Q[w] = d                    # set/update dgs
                    P[w] = v                    # set/update predecessor
    return D, P

def get_cost(dist, goal):
    for routers in  dist.keys():
        if routers == goal:
            return dist[routers]
    


def shortest_path(G, start, end):
    dist, pred = dijkstra(G, start, end)
    print(dist)
    v = end
    path = [v]
    while v != start:
        v = pred[v]
        path.append(v)        
    path.reverse()
    cost = get_cost(dist,end)
    return path, cost











if __name__ == '__main__':
    
    graph = r.Graph()
    graph.add_router("a", "b", 7)
    graph.add_router("a", "c", 9)
    graph.add_router("a", "f", 14)
    graph.add_router("b", "c", 10)
    graph.add_router("b", "d", 15)
    graph.add_router("c", "d", 11)
    graph.add_router("c", "f", 2)
    graph.add_router("d", "e", 6)
    graph.add_router("e", "f", 9)
    router = r.Router("a", graph)
    print(graph.router_list)
    

    # get shortest path distances to each node in `graph` from `a
    print(shortest_path(graph, "a", "b"))
