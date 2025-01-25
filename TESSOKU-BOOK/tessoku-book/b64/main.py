import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    
    n, m = map(int, input().split())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    edges = list()
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    graph.add_weighted_edges_from(edges)
    ans = nx.dijkstra_path(G=graph, source=1, target=n)
    print(*ans)

if __name__ == '__main__':
    main()
