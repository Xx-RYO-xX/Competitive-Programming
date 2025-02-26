import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    
    n = int(input())
    g = nx.Graph()
    edge = []
    for i in range(1, n+1):
        c = input()
        for j in range(1, n+1):
            if c[j-1] != "-":
                edge.append((i, j, c[j-1]))

    g.add_weighted_edges_from(edge)

    


if __name__ == '__main__':
    sys.exit(main())
