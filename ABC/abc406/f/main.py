import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx

    n = int(input())
    # 無向グラフに変更
    g = nx.Graph()
    g.add_nodes_from(range(1, n+1))
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v, 1))
    g.add_weighted_edges_from(edges)
    # 各頂点の初期重みを1で設定
    for u in g.nodes():
        g.nodes[u]['weight'] = 1

    q = int(input())
    for _ in range(q):
        tmp = input().split()
        if tmp[0] == "1":
            # 頂点 x の重みを w 増加
            x, w = map(int, tmp[1:])
            g.nodes[x]['weight'] += w
        else:
            # 辺 y を仮に外して成分を分ける
            y = int(tmp[1]) - 1
            u, v, _ = edges[y]
            gt = g.copy()
            gt.remove_edge(u, v)
            # u 側の成分
            comp = nx.node_connected_component(gt, u)
            s1 = sum(gt.nodes[n]['weight'] for n in comp)
            # もう一方の成分
            s2 = sum(gt.nodes[n]['weight'] for n in gt.nodes() if n not in comp)
            print(abs(s1 - s2))


if __name__ == '__main__':
    sys.exit(main())
