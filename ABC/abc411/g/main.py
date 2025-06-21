import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    n, m = map(int, input().split())
    MOD = 998244353
    g = nx.MultiGraph()
    
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    g.add_edges_from(edges)


if __name__ == '__main__':
    main()
