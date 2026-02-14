import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    from collections import deque

    n, m = map(int, input().split())
    c = sorted(map(int, input().split()))
    r = deque(sorted(map(int, input().split())))
    ans = 0
    for i in range(n):
        if r:
            while r and c[i] > r[0]:
                r.popleft()
            if r and c[i] <= r[0]:
                ans += 1
                r.popleft()

    print(ans)


if __name__ == "__main__":
    main()
