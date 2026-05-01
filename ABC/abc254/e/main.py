import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    for _ in range(int(input())):
        x, k = map(int, input().split())

        q = deque([(x, 0)])
        visited = {x}
        ans = x

        while q:
            pos, dep = q.popleft()
            if dep == k:
                continue

            for nxt in g[pos]:
                if nxt not in visited:
                    visited.add(nxt)
                    ans += nxt
                    q.append((nxt, dep + 1))

        print(ans)


if __name__ == "__main__":
    main()
