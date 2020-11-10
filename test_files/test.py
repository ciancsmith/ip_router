import dijkstras as di
import router as r

def main():   
    S, T, A, B, C, D, E, F, G = nodes = list("STABCDEFG")

    graph = r.Graph()
    graph.add_edge(S, A, 4)
    graph.add_edge(S, B, 3)
    graph.add_edge(S, D, 7)
    graph.add_edge(A, C, 1)
    graph.add_edge(B, S, 3)
    graph.add_edge(B, D, 4)
    graph.add_edge(C, E, 1)
    graph.add_edge(C, D, 3)
    graph.add_edge(D, E, 1)
    graph.add_edge(D, T, 3)
    graph.add_edge(D, F, 5)
    graph.add_edge(E, G, 2)
    graph.add_edge(G, E, 2)
    graph.add_edge(G, T, 3)
    graph.add_edge(T, F, 5)

dijkstra = DijkstraSPF(graph, S)

if __name__ == "__main__":
    main()