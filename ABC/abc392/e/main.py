import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    import matplotlib.pyplot as plt

    n, m = map(int, input().split())
    server = nx.MultiGraph()
    server.add_nodes_from(range(1, n+1))
    for i in range(1, m+1):
        a, b = map(int, input().split())
        server.add_edge(a, b, idx=i)

    


if __name__ == '__main__':
    import sys
    sys.exit(main())
