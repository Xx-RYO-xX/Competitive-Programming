import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    n, q = map(int, input().split())
    graph = nx.Graph()
    graph.add_node_from(range(1, n+1))
    edges = []
    for i in range(n-1):
        a, b = map(int, input().split())
        edges.append(a, b)
    edges.append(edges)

if __name__ == '__main__':
    sys.exit(main())
