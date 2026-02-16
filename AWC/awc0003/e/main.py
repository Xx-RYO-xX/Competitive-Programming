import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, m = map(int, input().split())
    w = deque(sorted(map(int, input().split()), reverse=True))
    c = list(map(int, input().split()))

    sys.setrecursionlimit(10**9)

    def dfs(ww, cc):
        if len(ww) == 0:
            print("Yes")
            exit()

        if sum(ww) > sum(cc):
            print("No")
            exit()

        seen = set()

        for j in range(m):
            if cc[j] - ww[0] >= 0:
                if cc[j] in seen:
                    continue
                seen.add(cc[j])

                cc[j] -= ww[0]
                tmp = ww.popleft()
                dfs(ww, cc)
                ww.appendleft(tmp)
                cc[j] += ww[0]

    dfs(w, c)
    print("No")


if __name__ == "__main__":
    main()
