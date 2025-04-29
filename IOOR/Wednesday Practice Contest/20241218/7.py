def main():
    import networkx as nx
    # import matplotlib.pyplot as plt
    
    n = int(input())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(n-1):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    graph.add_weighted_edges_from(edges)
    # nx.draw_networkx(graph)
    # plt.show()
    
    q, k = map(int, input().split())
    distances = nx.single_source_dijkstra_path_length(G=graph, source=k)
    for _ in range(q):
        x, y = map(int, input().split())
        x_to_k = distances.get(x, float('inf'))
        k_to_y = distances.get(y, float('inf'))
        
        print(x_to_k+k_to_y)

if __name__ == '__main__':
    main()