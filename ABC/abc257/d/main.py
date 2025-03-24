import sys
import decimal


def input():return sys.stdin.readline().rstrip()


def rounding(num, digit):
    """
    四捨五入を正確にする関数

    Parameters
    ----------
    num : float or int or str
        四捨五入したい数
    digit : int
        丸める桁数

    Returns
    -------
    return : decimal.Decimal
        四捨五入された数値

    Notes
    -----
    - digitが2以上の場合(2桁目以降に丸める時)、指数表記になるのでキャストが必要
    """
    deci = 10 ** digit if digit != 0 else 0
    return (decimal.Decimal(str(num)).
            quantize(decimal.Decimal(str(deci) if deci < 1 else "1E" + str(digit - 1)), decimal.ROUND_HALF_UP))




def main():
    import networkx as nx
    # import matplotlib.pyplot as plt
    

    n = int(input())
    x, y, p = [], [], []
    for _ in range(n):
        xt, yt, pt = map(int, input().split())
        x.append(xt)
        y.append(yt)
        p.append(pt)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            weight = abs(x[i]-x[j]) + abs(y[i]-y[j])
            edges.append((i, j, weight/p[i]))
            edges.append((j, i, weight/p[j]))
    g = nx.DiGraph()
    g.add_nodes_from(range(n))
    g.add_weighted_edges_from(edges)
    
    path = nx.all_pairs_dijkstra_path_length(g)
    ans = float("inf")
    for p in path:
        i, path_len = p
        ans = min(ans, max(path_len.values()))

    print(ans)

if __name__ == '__main__':
    main()
