import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    n = int(input())
    g = nx.Graph()
    g.add_nodes_from(range(1, n+1))
    edge = []
    for i in range(n-1):
        a, b = map(int, input().split())
        edge.append((a, b))
    g.add_edges_from(edge)


if __name__ == '__main__':
    sys.exit(main())
