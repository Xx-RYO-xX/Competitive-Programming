def main():
    import networkx as nx
    import matplotlib.pyplot as plt

    n = int(input())
    
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edge = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edge.append((u, v))
    graph.add_edges_from(edge)
    
    nx.draw_networkx(graph)
    plt.show()


if __name__ == '__main__':
    main()