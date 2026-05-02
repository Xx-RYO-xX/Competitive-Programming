import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        g = [[] for _ in range(n + 1)]
        for __ in range(m):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)
        w = int(input())
        s = [""]
        for ___ in range(n):
            s.append(input())

        def choten(u, day):
            return (u - 1) * w + day

        week_g = [[] for _ in range(w * n)]
        for u in range(1, n + 1):
            for day in range(w):
                nday = (day + 1) % w
                if s[u][nday] == "o":
                    week_g[choten(u, day)].append(choten(u, nday))
                for nex in g[u]:
                    if s[nex][nday] == "o":
                        week_g[choten(u, day)].append(choten(nex, nday))

        ## https://qiita.com/karutetto332/items/c1b407aece3e17b2f835
        cycle = False

        sys.setrecursionlimit(10**9)

        def dfs(g, crr, visited, finished):
            visited[crr] = True
            for nxt in g[crr]:
                if not visited[nxt]:
                    dfs(g, nxt, visited, finished)
                elif not finished[nxt]:
                    nonlocal cycle
                    cycle = True
            finished[crr] = True

        visited = [False] * (w * n)
        finished = [False] * (w * n)
        for crr in range(0, w * n, w):
            u = crr // w + 1
            if s[u][0] == "o" and not visited[crr]:
                dfs(week_g, crr, visited, finished)

        print("Yes" if cycle else "No")


if __name__ == "__main__":
    main()
