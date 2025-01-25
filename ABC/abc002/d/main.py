import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    from itertools import combinations
    
    n, m = map(int, input().split())
    habatsu = nx.Graph()
    habatsu.add_nodes_from(range(1, n+1))
    edge = []
    for _ in range(m):
        x, y = map(int, input().split())
        edge.append((x, y))
    habatsu.add_edges_from(edge)
    
    ans = 0

    for k in range(1, n+1):
        for subset in combinations(range(1, n+1), k):
            if all(habatsu.has_edge(x, y) for x, y in combinations(subset, 2)):
                ans = max(ans, k)
    print(ans)


if __name__ == '__main__':
    sys.exit(main())
