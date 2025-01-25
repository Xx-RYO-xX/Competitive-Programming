import sys


def input():return sys.stdin.readline().rstrip()


def main():
    import networkx as nx
    h, w, k = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    
    masu = nx.grid_2d_graph(w, h)
    ans = 0

    print(ans)


if __name__ == '__main__':
    main()
