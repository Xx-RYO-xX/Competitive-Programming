import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    q = int(input())
    tutu = deque([])
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que, x, c = map(int, query)
            tutu.append([x, c])
        else:
            que, c = map(int, query)
            ans = 0
            while tutu[0][1] < c:
                x, cc = tutu.popleft()
                ans += x * cc
                c -= cc
            ans += tutu[0][0] * c
            tutu[0][1] -= c
            print(ans)


if __name__ == "__main__":
    sys.exit(main())
