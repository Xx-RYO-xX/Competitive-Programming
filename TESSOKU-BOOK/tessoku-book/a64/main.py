import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    
    n, m = map(int, input().split())
    graph = nx.Graph()
    graph.add_nodes_from(range(1, n+1))
    egdes = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        egdes.append((a, b, c))
    graph.add_weighted_edges_from(egdes)
    
    distances = nx.single_source_dijkstra_path_length(G=graph, source=1)
    for i in range(1, n+1):
        print(distances.get(i, "-1"))


if __name__ == '__main__':
    main()
