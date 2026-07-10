from posixpath import sep
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n, t = map(int, input().split())
    ans = 0
    for _ in range(n):
        a, c = map(int, input().split())
        if t <= a:
            continue
        ans += (t - a) * c

    print(ans)


if __name__ == "__main__":
    main()
