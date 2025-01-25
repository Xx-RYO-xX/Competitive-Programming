def main():
    import networkx as nx
    # import matplotlib.pyplot as plt
    
    n, m = map(int, input().split())
    graph = nx.DiGraph()
    graph.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
        edges.append((b, a))
    graph.add_edges_from(edges)
    
    ans = list(nx.strongly_connected_components(graph))
    # print(ans)
    print(len(ans)-1)
    
    # nx.draw_networkx(graph)
    # plt.show()
    

if __name__ == '__main__':
    main()