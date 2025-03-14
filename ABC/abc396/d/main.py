import sys


def input():return sys.stdin.readline().rstrip()

def main():
    import networkx as nx
    sys.setrecursionlimit(10**7)
    n, m = map(int, input().split())
    g = nx.Graph()
    g.add_nodes_from(range(1, n+1))

    for _ in range(m):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, weight=w)

    ans = float('inf')
    for path in nx.all_simple_paths(g, source=1, target=n):
        tmp_xor = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            tmp_xor ^= g[u][v]['weight']
        ans = min(ans, tmp_xor)

    print(ans if ans != float('inf') else 0)


if __name__ == '__main__':
    sys.exit(main())