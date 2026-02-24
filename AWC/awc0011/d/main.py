import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, input().split())
    v = [0] + list(map(int, input().split()))
    p = list(map(int, input().split()))
    g = list([] for _ in range(n + 1))
    for i in range(n - 1):
        g[i + 2].append(p[i])

    sisann = [-1] * (n + 1)

    sys.setrecursionlimit(10**9)

    def dfs(x, sums=0):
        if x == 1:
            return sums + v[1]
        for nex in g[x]:
            if sisann[nex] == -1:
                nex_value = dfs(nex, sums + v[x])
                sisann[x] = nex_value - sums
                return nex_value
            else:
                return sisann[nex] + sums + v[x]

    for _ in range(q):
        x = int(input())
        sisann[x] = dfs(x)
        print(sisann[x])


if __name__ == "__main__":
    main()
