import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    from itertools import permutations
    
    n, m = map(int, input().split())
    g = nx.Graph()
    g.add_nodes_from(range(1, n+1))
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    g.add_edges_from(edges)
    
    ans = float('inf')
    for perm in permutations(range(1, n+1)):
        visited = set()
        cond = True
        dg_edges = []
        for i in range(1, n+1):
            if i not in visited:
                cycle = []
                idx = i
                while idx not in visited:
                    visited.add(idx)
                    cycle.append(idx)
                    idx = perm[idx-1]
                if idx != i or len(cycle) < 3:
                    cond = False
                    break
                for j in range(len(cycle)):
                    u = cycle[j]
                    v = cycle[(j+1) % len(cycle)]
                    dg_edges.append((u, v))

        if not cond:
            continue
        dg = nx.Graph()
        dg.add_edges_from(dg_edges)
        diff = nx.symmetric_difference(g, dg)
        anst = diff.number_of_edges()
        ans = min(ans, anst)
    print(ans)
    


if __name__ == '__main__':
    main()
