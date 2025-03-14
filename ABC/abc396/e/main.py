import sys


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import deque
    import networkx as nx
    
    n, m = map(int, input().split())
    g = nx.Graph()
    
    used = {}
    
    g.add_nodes_from(range(n))
    
    edges = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        if x == y and z != 0:
            print(-1)
            return
        
        if (x, y) in used or (y, x) in used:
            tmp_z = used.get((x, y), used.get((y, x)))
            if tmp_z != z:
                print(-1)
                return
        else:
            used[(x, y)] = z
        
        edges.append((x, y, z))
    g.add_weighted_edges_from(edges)
    
    ans = [-1] * n
    
    for comp in nx.connected_components(g):
        start = next(iter(comp))
        if ans[start] < 0:
            ans[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in g[u]:
                    w = g[u][v]['weight']
                    if ans[v] < 0:
                        ans[v] = ans[u] ^ w
                        queue.append(v)
                    elif ans[v] != (ans[u] ^ w):
                        print(-1)
                        return
    
    print(*ans)

if __name__ == '__main__':
    sys.exit(main())
