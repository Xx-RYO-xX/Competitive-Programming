import sys


def input():return sys.stdin.readline().rstrip()


def find(g, start_node, length):
    paths = []

    def dfs(path):
        if len(path) == length + 1:
            paths.append(path[:])
            return

        for next in g.neighbors(path[-1]):
            path.append(next)
            dfs(path)
            path.pop()

    dfs([start_node])
    return paths


def main():
    import networkx as nx
    n, m = map(int, input().split())
    g = nx.Graph()
    g.add_nodes_from(range(1, n+1))
    for _ in range(m):
        a, b = map(int, input().split())
        g.add_edge(a, b)
    s = input()

    ans = 0
    
    for i in range(1, n+1):
        path = find(g, i, 4)
        # print(path)
        for p in path:
            ss = ""
            for pp in p:
                ss += s[pp-1]
            if ss == ss[::-1]:
                print(p)
                ans += 1


    print(ans)


if __name__ == '__main__':
    main()

