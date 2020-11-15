from pqdict import PQDict


class Router:
    """Router class that implements a node like model for a graph object"""

    def __init__(self, name, graph):
        self.name = name
        self.graph = graph

    def get_path(self, dst):
        path, cost = self.graph.shortest_path(self.name, dst)
        start = path[0]
        finish = path[len(path) - 1]
        print("Start: {}\nEnd: {}\nPath: {}\nCost: {}".format(
            start, finish, "->".join(path), cost))
        return start, finish, path, cost

    def print_routing_table(self):
        pos = 0
        info = {}
        router_list = self.graph.get_routers()
        for routers in router_list:
            if routers != self.name:
                path, cost = self.graph.shortest_path(self.name, routers)
                info[pos] = [self.name, routers, cost, "->".join(path)]
            pos += 1
        print("{:<8}{:<8} {:<10} {:<10} {:<10}".format(
            "pos", "from", "to", "cost", "path"))
        for k, v in info.items():
            From, to, cost, path = v
            print("{:<8}{:<8} {:<10} {:<10} {:<10}".format(
                k, From, to, cost, path))

        return path, cost, info


class Graph(object):

    def __init__(self, adjacency_list=dict(), edge_weights=dict()):
        """Initialises graph object"""
        self.router_list = adjacency_list
        self.router_cost = edge_weights

    def add_router(self, router_a, router_b, cost):
        """ Add a new router router_a -> router_b to graph with edge weight. """
        self.router_cost[router_a, router_b] = cost
        if router_a not in self.router_list:
            self.router_list[router_a] = dict()
        if router_b not in self.router_list:
            self.router_list[router_b] = dict()
        self.router_list[router_a][router_b] = cost
        self.router_list[router_b][router_a] = cost

    def remove_router(self, router):
        """Removes router provided from the graph object """
        copy_list = self.router_list.copy()
        temp_dict = {}
        for k, v in copy_list.items():
            if k == router:
                continue
            else:
                temp_dict[k] = {}
                for k2, v2 in v.items():
                    if k2 == router:
                        continue
                    else:
                        temp_dict[k][k2] = v2

        self.router_list = temp_dict

    def get_router_cost(self, router_a, router_b):
        """ Get router cost of edge between router_a and router_b. """
        return self.router_cost[router_a, router_b]

    def get_adjacent_routers(self, router):
        """ Get routers adjacent to router. """
        return self.router_list.get(router, list())

    def get_number_of_routers(self):
        """ Return the total number of nodes in graph. """
        return len(self.router_list)

    def get_routers(self):
        """ Return all nodes in this graph. """
        return self.router_list

    def dijkstra(self, src, dst):
        """dijkstras algorithm used to calculate the shortest path between two nodes a Priority queue is used in this implementation"""
        inf = float('inf')
        D = {src: 0}
        Q = PQDict(D)
        P = {}
        U = set(self.router_list)

        while U:
            (v, d) = Q.popitem()
            D[v] = d
            U.remove(v)
            if str(v) == dst:
                break

            for w in self.router_list[v]:
                if w in U:

                    d = D[v] + self.router_list[v][w]
                    if d < Q.get(w, inf):
                        Q[w] = d
                        P[w] = v

        return D, P

    def get_cost(self, dist, goal):
        """get the cost hgelper function for shortest path"""
        for routers in dist.keys():
            if routers == goal:
                return dist[routers]

    def shortest_path(self, start, end):
        """uses dijkstras algorithim to find the shortest path"""
        dist, pred = self.dijkstra(start, end)
        v = end
        path = [v]
        while v != start:
            v = pred[v]
            path.append(v)
        path.reverse()
        cost = self.get_cost(dist, end)
        return path, cost


if __name__ == "__main__":
    graph = Graph()
    graph.add_router("a", "b", 7)
    graph.add_router("a", "c", 9)
    graph.add_router("a", "f", 14)
    graph.add_router("b", "c", 10)
    graph.add_router("b", "d", 15)
    graph.add_router("c", "d", 11)
    graph.add_router("c", "f", 2)
    graph.add_router("d", "e", 6)
    graph.add_router("e", "f", 9)

    router = Router("a", graph)
    router.get_path("b")
    router.print_routing_table()
    print(graph.router_list)
    graph.remove_router("c")
    print(graph.router_list)
    router.print_routing_table()
