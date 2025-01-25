import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    
    n, m, k = map(int, input().split())
    G = nx.Graph()
    G.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    G.add_weighted_edges_from(edges)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


if __name__ == '__main__':
    main()
