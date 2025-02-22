import sys 


def input():return sys.stdin.readline().rstrip()


def main():
    from collections import defaultdict
    import networkx as nx

    n, m = map(int, input().split())
    edge = defaultdict(int)
    ans = 0
    for _ in range(m):
        u, v, = map(int, input().split())
        if u == v:
            ans += 1
        else:
            if (u, v) in edge or (v, u) in edge:
                ans += 1
            else:
                edge[(u, v)] += 1

    print(ans)




if __name__ == '__main__':
    sys.exit(main())
