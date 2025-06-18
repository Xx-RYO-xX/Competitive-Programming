import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    from collections import deque
    
    n, m = map(int, input().split())
    g = nx.DiGraph()
    
    edges = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))
    g.add_weighted_edges_from(edges)

    dist = {i: None for i in range(1, n+1)}
    dist[1] = 0
    dq = deque([1])
    while dq:
        u = dq.popleft()
        for _, v, _, data in g.out_edges(u, data=True, keys=True):
            if dist[v] is None:
                dist[v] = dist[u] ^ data['weight']
                dq.append(v)
    if dist[n] is None:
        print(-1)
        return

    rev = g.reverse(copy=False)
    reach = {n}
    dq = deque([n])
    while dq:
        u = dq.popleft()
        for p in rev.successors(u):
            if p not in reach:
                reach.add(p)
                dq.append(p)
    
    cycle = []
    for u, v, _, data in g.edges(keys=True, data=True):
        if dist.get(u) is None or dist.get(v) is None:
            continue
        
        if u not in reach or v not in reach: 
            continue
        
        cycle.append(dist[u]^data['weight']^dist[v])
    
    bit = []
    for x in cycle:
        for b in bit:
            x = min(x, x^b)
        if x:
            bit.append(x)
    ans = dist[n]
    for b in bit:
        ans = min(ans, ans^b)
        
        
    print(ans)
    

if __name__ == '__main__':
    sys.exit(main())
